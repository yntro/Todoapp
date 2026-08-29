from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('my_tasks/', views.MyTasksView.as_view(), name='my_tasks'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
]