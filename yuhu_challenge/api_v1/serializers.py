from rest_framework import serializers
from todos.models import ToDoItem


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = "__all__"


class ToDoListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = [
            "id",
            "name",
            "description",
            "user",
        ]


class ToDoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = "__all__"
