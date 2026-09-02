from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('my_tasks/', views.MyTasksView.as_view(), name='my_tasks'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('admin/', views.AdminView.as_view() ,name='admin'),
    path('admin/users/<int:pk>/', views.AdminUserUpdateView.as_view(), name='admin_user'),
    path('admin/teams/update/<int:pk>/', views.TeamUpdateView.as_view(), name='team_update'),
    path('admin/teams/delete/<int:pk>/', views.TeamDeleteView.as_view(), name='team_delete'),
    path('admin/teams/create/', views.TeamCreateView.as_view(), name='team_create'),
    path('team_tasks/', views.TeamTasksView.as_view(), name='team_tasks'),
    path('team_tasks/create/', views.TeamTasksCreateView.as_view(), name='team_tasks_create'),
    path('team_tasks/update/<int:pk>', views.TeamTasksUpdateView.as_view(), name='team_tasks_update'),
    path('team_tasks/delete/<int:pk>', views.TeamTasksDeleteView.as_view(), name='team_tasks_delete'),
]