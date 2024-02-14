from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_list, name='todos_list'),
    path('create/', views.create_todo, name='create_todo'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),  # Используйте pk вместо id
    path('<int:pk>/delete/', views.delete_todo, name='delete_todo'),
    path('<int:pk>/update/', views.update_todo, name='update_todo'),
]
