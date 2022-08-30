from django.urls import path
from .views import taskform, taskview, update, delete_view

urlpatterns = [
    path('', taskview, name='taskview-page'),
    path('taskform/', taskform, name='taskform-page'),
    path('update/<int:id>', update, name='taskupdate-page'),
    path('delete/<int:id>', delete_view, name='delete'),
]