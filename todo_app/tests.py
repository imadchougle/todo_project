from django.test import TestCase
from todo_app.models import Todo, Tag

class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(title='Test Todo', description='Test description')
        self.assertEqual(str(todo), 'Test Todo')


class TagModelTest(TestCase):
    def test_create_tag(self):
        tag = Tag.objects.create(name='Test Tag')
        self.assertEqual(str(tag), 'Test Tag')

from django.test import TestCase
from todo_app.serializers import TodoSerializer

class TodoSerializerTest(TestCase):
    def test_valid_serializer_data(self):
        valid_data = {'title': 'Test Todo', 'description': 'Test description'}
        serializer = TodoSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

from django.test import TestCase
from django.urls import reverse
from todo_app.models import Todo, Tag

class TodoListViewTest(TestCase):
    def test_todo_list_view(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list.html')