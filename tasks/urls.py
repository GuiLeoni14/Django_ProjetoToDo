from django.urls import path
from .views import hellouworld, tasks_list, yourname
from . import views

urlpatterns = [
    path('hellouworld/', hellouworld),
    path('', tasks_list, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('delete/<int:id>', views.deleteTask, name='delete-task'),
    path('yourname/<str:name>', yourname, name='yourname'),
]