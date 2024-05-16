from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import ToDoItem
from .serializers import ToDoItemSerializer


class ToDoListCreate(ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


class ToDoDetail(RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
