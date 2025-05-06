from django.contrib import admin

from .models import Task, Group, Table


admin.site.register(Table)
admin.site.register(Group)
admin.site.register(Task)