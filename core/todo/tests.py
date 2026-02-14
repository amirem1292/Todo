from django.test import TestCase

from todo.forms import LoginForm, TaskUpdateForm
from django.contrib.auth.models import User
from .models import Task

# Create your tests here.

# forms
class FormTests(TestCase):

    def test_task_update_form_with_valid_data(self):
        form = TaskUpdateForm(data={'is_done':True})
        self.assertTrue(form.is_valid())

    def test_login_form_with_valid_data(self):
        form = LoginForm( data = { 'username' : 'admin', 'password' : 'admin' } )
        self.assertTrue(form.is_valid())



# models
class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='')

    def test_task_model_with_valid_data(self):
        task = Task.objects.create(
            author = self.user,
            title = 'Task 1',
            is_done = False,
        )
        self.assertAlmostEqual(task.is_done, False)