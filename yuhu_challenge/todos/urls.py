from django.urls import path

from .views import CombinedTodoView, ToDoDeleteView, ToDoUpdateView, ToogleToDoView

app_name = "todos"

urlpatterns = [
    path("delete/<int:pk>", ToDoDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", ToDoUpdateView.as_view(), name="update"),
    path("toggle_is_done/<int:pk>/", ToogleToDoView.as_view(), name="toggle_is_done"),
    path("", CombinedTodoView.as_view(), name="list"),
]
