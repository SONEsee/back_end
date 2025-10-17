
from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = 'Create optimized database indexes for customer search on utility database'

    def handle(self, *args, **options):
        # Use 'utility' database connection
        with connections['utility'].cursor() as cursor:
            try:
                self.stdout.write('Creating indexes on utility database...')
                
                # For PostgreSQL - Create GIN index for full-text search
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS edl_customer_name_gin 
                    ON edl_customer_info 
                    USING gin(to_tsvector('simple', 
                        COALESCE(Name, '') || ' ' || 
                        COALESCE(Surname, '') || ' ' || 
                        COALESCE(Company_name, '')
                    ))
                """)
                self.stdout.write(self.style.SUCCESS('✓ Created GIN index for full-text search'))
                
                # Create standard B-tree indexes
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS edl_customer_id_idx 
                    ON edl_customer_info (Customer_ID)
                """)
                self.stdout.write(self.style.SUCCESS('✓ Created index on Customer_ID'))
                
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS edl_name_idx 
                    ON edl_customer_info (Name)
                """)
                self.stdout.write(self.style.SUCCESS('✓ Created index on Name'))
                
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS edl_surname_idx 
                    ON edl_customer_info (Surname)
                """)
                self.stdout.write(self.style.SUCCESS('✓ Created index on Surname'))
                
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS edl_company_idx 
                    ON edl_customer_info (Company_name)
                """)
                self.stdout.write(self.style.SUCCESS('✓ Created index on Company_name'))
                
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS edl_province_idx 
                    ON edl_customer_info (Province_ID)
                """)
                self.stdout.write(self.style.SUCCESS('✓ Created index on Province_ID'))
                
                # Composite indexes for faster filtered searches
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS edl_name_province_idx 
                    ON edl_customer_info (Name, Province_ID)
                """)
                self.stdout.write(self.style.SUCCESS('✓ Created composite index on Name + Province_ID'))
                
                self.stdout.write(self.style.SUCCESS('\n✓ Successfully created all search indexes on utility database!'))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'\n✗ Error creating indexes: {str(e)}'))
                raise