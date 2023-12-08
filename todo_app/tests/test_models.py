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