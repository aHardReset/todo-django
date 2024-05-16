from django.urls import path

from .views import ToDoDetail, ToDoListCreate

app_name = "api_v1"

urlpatterns = [
    path("todos/", ToDoListCreate.as_view(), name="list"),
    path("todos/<int:pk>/", ToDoDetail.as_view(), name="detail"),
    # path("items", ToDoItemViewSet.as_view(), name="todos"),
]
