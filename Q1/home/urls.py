from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('tasks/', views.tasks, name = 'tasks'),
    path('taskAdd/', views.taskAdd, name = 'taskAdd'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutPage, name = 'logout'),
]