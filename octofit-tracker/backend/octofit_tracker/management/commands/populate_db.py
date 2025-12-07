from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User(email='captain@marvel.com', name='Captain Marvel', team='marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='running', duration=30, points=10, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='cycling', duration=45, points=15, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='swimming', duration=60, points=20, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='walking', duration=20, points=5, date=timezone.now().date())

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=25, month='December')
        Leaderboard.objects.create(team='dc', points=25, month='December')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
