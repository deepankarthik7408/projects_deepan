from django.urls import path
from .todo_view_elements.table import *
from .todo_view_elements.group import *
from .todo_view_elements.task import *

todo_patterns = [
    path('table', TablesAPI.as_view()), # tables list (get post patch delete)
    path('table/<int:id>', TableAPI.as_view()), # each table (get) (( if user opened table getting inner table data ))
    
    # (post patch delete)
    path('group', GroupAPI.as_view()), 
    path('task', TaskAPI.as_view())
]