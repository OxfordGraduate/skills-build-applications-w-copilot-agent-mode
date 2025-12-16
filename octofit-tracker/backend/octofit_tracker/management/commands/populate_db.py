from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Users
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@marvel.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@dc.com', password='batman', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman', team=dc)

        # Activities
        Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='cycle', duration=45, calories=400)
        Activity.objects.create(user=bruce, type='swim', duration=60, calories=500)
        Activity.objects.create(user=clark, type='run', duration=50, calories=450)

        # Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Leaderboard
        Leaderboard.objects.create(user=tony, score=300)
        Leaderboard.objects.create(user=steve, score=400)
        Leaderboard.objects.create(user=bruce, score=500)
        Leaderboard.objects.create(user=clark, score=450)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
