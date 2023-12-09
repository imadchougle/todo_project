from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from todo_app.models import Todo, Tag
from todo_app.serializers import TodoSerializer


class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(title='Test Todo',
                                   description='Test description')
        self.assertEqual(str(todo), 'Test Todo')


class TagModelTest(TestCase):
    def test_create_tag(self):
        tag = Tag.objects.create(name='Test Tag')
        self.assertEqual(str(tag), 'Test Tag')


class TodoSerializerTest(TestCase):
    def test_valid_serializer_data(self):
        valid_data = {'title': 'Test Todo', 'description': 'Test description'}
        serializer = TodoSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())


class TodoListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.accepted_media_type, 'application/json')
