from django.core.management.base import BaseCommand
from .models import Login, memberInfo  # Adjust to match your actual app name and model names
from django.utils import timezone

class Command(BaseCommand):
    help = 'Add users from memberInfo table'

    def handle(self, *args, **kwargs):
        # Fetch all rows from the memberInfo table
        members = memberInfo.objects.all()
        added_users = 0

        for member in members:
            try:
                # Create new user in the Login table
                user = Login.objects.create(
                    username=member.code,
                    nameL=member.nameL,
                    surnameL=member.nameL,  # As per your instructions
                    nameE=member.nameE,
                    surnameE=member.nameE,   # As per your instructions
                    GID_id=7,  # Assuming this is the default GID you want
                    MID=member,  # Set the MID as a ForeignKey to the memberInfo instance
                    is_active=True,
                    is_staff=False,
                    is_superuser=False,
                    insertDate=timezone.now(),
                    updateDate=timezone.now()
                )
                added_users += 1
                self.stdout.write(self.style.SUCCESS(f'Added user {user.username}'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Failed to add user for member {member.id}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully added {added_users} users.'))


