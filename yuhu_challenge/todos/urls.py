from django.urls import path

from .views import CombinedTodoView, ToDoDeleteView, ToDoUpdateView

app_name = "todos"

urlpatterns = [
    path("delete/<int:pk>", ToDoDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", ToDoUpdateView.as_view(), name="update"),
    path("", CombinedTodoView.as_view(), name="list"),
]
