from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import UserProfile

class Command(BaseCommand):
    help = 'Create UserProfile objects for users that don\'t have them'

    def handle(self, *args, **options):
        users_without_profiles = []
        
        for user in User.objects.all():
            if not hasattr(user, 'profile'):
                users_without_profiles.append(user)
        
        if not users_without_profiles:
            self.stdout.write(
                self.style.SUCCESS('All users already have profiles!')
            )
            return
        
        self.stdout.write(f'Found {len(users_without_profiles)} users without profiles')
        
        for user in users_without_profiles:
            # Determine user type based on superuser status
            if user.is_superuser:
                user_type = 'admin'
            else:
                user_type = 'student'
            
            # Create profile
            profile = UserProfile.objects.create(
                user=user,
                user_type=user_type
            )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Created profile for user "{user.username}" with type "{user_type}"'
                )
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(users_without_profiles)} profiles!')
        )
