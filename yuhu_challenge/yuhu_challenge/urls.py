from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("todos/", include("todos.urls")),
    path("api_v1/", include("api_v1.urls")),
]
