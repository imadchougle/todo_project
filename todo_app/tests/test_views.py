from django.test import TestCase
from django.urls import reverse
from todo_app.models import Todo, Tag

class TodoListViewTest(TestCase):
    def test_todo_list_view(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list.html')