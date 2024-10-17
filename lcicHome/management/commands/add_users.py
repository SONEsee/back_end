from django.core.management.base import BaseCommand
from lcicHome.models import Login 
from lcicHome.models import memberInfo # Adjust to match your actual app 
from django.utils import timezone

class Command(BaseCommand):
    help = 'Add users from memberInfo table'

    def handle(self, *args, **kwargs):
        # Fetch all rows from the memberInfo table
        members = memberInfo.objects.all()
        added_users = 0
        default_password = '12345678'  # Set your default password here

        for member in members:
            try:
                # Create new user using create_user() to hash the password
                user = Login.objects.create_user(
                    username=member.code,
                    password=default_password,  # Password will be hashed inside create_user
                    MID=member,  # Set the MID as a ForeignKey to the memberInfo instance
                    GID_id=7,  # Assuming this is the default GID you want
                    nameL=member.nameL,
                    surnameL=member.nameL,  # As per your instructions
                    nameE=member.nameE,
                    surnameE=member.nameE,   # As per your instructions
                    is_active=True,
                    is_staff=False,
                    is_superuser=False,
                    insertDate=timezone.now(),
                    updateDate=timezone.now()
                )

                added_users += 1
                self.stdout.write(self.style.SUCCESS(f'Added user {user.username} with default password'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Failed to add user for member {member.id}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully added {added_users} users.'))