from django.test import TestCase
from todo_app.serializers import TodoSerializer

class TodoSerializerTest(TestCase):
    def test_valid_serializer_data(self):
        valid_data = {'title': 'Test Todo', 'description': 'Test description'}
        serializer = TodoSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())