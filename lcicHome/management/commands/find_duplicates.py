from django.core.management.base import BaseCommand
from django.db import transaction
from ...matching_service import CustomerMatchingService


class Command(BaseCommand):
    help = 'Find and save potential duplicate customers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--min-score',
            type=float,
            default=60.0,
            help='Minimum similarity score (0-100)',
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=1000,
            help='Maximum number of records to process',
        )
        parser.add_argument(
            '--save',
            action='store_true',
            help='Save candidates to database',
        )
        parser.add_argument(
            '--auto-merge',
            type=float,
            default=None,
            help='Auto-merge candidates above this score (e.g., 95)',
        )

    def handle(self, *args, **options):
        min_score = options['min_score']
        limit = options['limit']
        save = options['save']
        auto_merge_score = options['auto_merge']

        self.stdout.write(self.style.SUCCESS(
            f'Starting duplicate detection (min_score={min_score}, limit={limit})...'
        ))

        # Import models
        from ...models import IndividualBankIbk, MatchingCandidate
        from ...merge_service import CustomerMergeService
        
        # Find matches
        candidates = CustomerMatchingService.find_matches(
            IndividualBankIbk,
            limit=limit,
            min_score=min_score
        )

        self.stdout.write(self.style.SUCCESS(
            f'Found {len(candidates)} potential matches'
        ))

        if not candidates:
            self.stdout.write(self.style.WARNING('No matches found'))
            return

        # Save to database
        if save:
            saved_count = 0
            auto_merged_count = 0
            
            for candidate in candidates:
                # Save candidate
                mc, created = MatchingCandidate.objects.update_or_create(
                    source_ind_sys_id=candidate['source_ind_sys_id'],
                    target_ind_sys_id=candidate['target_ind_sys_id'],
                    defaults={
                        'source_lcic_id': candidate['source_lcic_id'],
                        'target_lcic_id': candidate['target_lcic_id'],
                        'similarity_score': candidate['similarity_score'],
                        'match_details': candidate['match_details'],
                        'status': 'PENDING',
                    }
                )
                
                if created:
                    saved_count += 1
                
                # Auto-merge if score is high enough
                if auto_merge_score and candidate['similarity_score'] >= auto_merge_score:
                    try:
                        from ...models import IndividualBankIbkInfo, IndividualIdentifier, MergeHistory
                        
                        CustomerMergeService.merge_customers(
                            IndividualBankIbk=IndividualBankIbk,
                            IndividualBankIbkInfo=IndividualBankIbkInfo,
                            IndividualIdentifier=IndividualIdentifier,
                            MergeHistory=MergeHistory,
                            source_ids=[
                                candidate['source_ind_sys_id'],
                                candidate['target_ind_sys_id']
                            ],
                            performed_by='system_auto',
                            reason=f'Auto-merged (score: {candidate["similarity_score"]})'
                        )
                        
                        mc.status = 'AUTO_MATCHED'
                        mc.reviewed_by = 'system_auto'
                        mc.save()
                        
                        auto_merged_count += 1
                        
                        self.stdout.write(self.style.SUCCESS(
                            f'Auto-merged: {candidate["source_ind_sys_id"]} + {candidate["target_ind_sys_id"]} (score: {candidate["similarity_score"]})'
                        ))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(
                            f'Failed to auto-merge: {str(e)}'
                        ))

            self.stdout.write(self.style.SUCCESS(
                f'Saved {saved_count} candidates to database'
            ))
            
            if auto_merge_score:
                self.stdout.write(self.style.SUCCESS(
                    f'Auto-merged {auto_merged_count} high-confidence matches'
                ))
        else:
            # Print top matches
            self.stdout.write('\nTop 10 Matches:')
            for i, candidate in enumerate(candidates[:10], 1):
                self.stdout.write(
                    f"{i}. Score: {candidate['similarity_score']:.2f} - "
                    f"IDs: {candidate['source_ind_sys_id']} + {candidate['target_ind_sys_id']}"
                )
            
            self.stdout.write(self.style.WARNING(
                '\nUse --save to save candidates to database'
            ))

        self.stdout.write(self.style.SUCCESS('Done!'))
