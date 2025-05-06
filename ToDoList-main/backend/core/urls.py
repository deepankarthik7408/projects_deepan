from django.contrib import admin
from django.urls import path, include

from user.urls import user_patterns
from todo.urls import todo_patterns


urlpatterns = [
    path("admin/", admin.site.urls),

    path("user/", include(user_patterns)),
    path("todo/", include(todo_patterns))
]
