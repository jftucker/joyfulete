from django.test import Client, TestCase
from django.urls import reverse

from .models import Workout, Tag


class WorkoutTests(TestCase):

    def setUp(self):
        self.workout = Workout.objects.create(
            title='test workout',
            description='test description',
        )
        self.tag = Tag.objects.create(
            tag = 'Test Tag'
        )
        self.tag.workouts.add(self.workout)

    
    def test_workout_listing(self):
        self.assertEqual(f'{self.workout.title}', 'test workout')
        self.assertEqual(f'{self.workout.description}', 'test description')

    def test_workout_list_view(self):
        response = self.client.get(reverse('workout_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test workout')
        self.assertTemplateUsed(response, 'workouts/workout_list.html')

    def test_workout_detail_view(self):
        response = self.client.get(self.workout.get_absolute_url())
        no_response = self.client.get('/workouts/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test workout')
        self.assertContains(response, 'Test Tag')
        self.assertTemplateUsed(response, 'workouts/workout_detail.html')