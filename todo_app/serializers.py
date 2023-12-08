from rest_framework import serializers
from .models import Todo, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Todo
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        todo_instance = Todo.objects.create(**validated_data)

        tags = []
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data.get('name'))
            tags.append(tag)

        todo_instance.tags.set(tags)
        return todo_instance
