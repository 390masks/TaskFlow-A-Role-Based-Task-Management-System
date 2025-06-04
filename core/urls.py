from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    # Auth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Users & Teams
    path('users/', UserListView.as_view(), name='user_list'),
    path('teams/', TeamView.as_view(), name='team_list'),

    # Projects & Tasks
    path('projects/', ProjectView.as_view(), name='project_list'),
    path('tasks/', TaskView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskUpdateDeleteView.as_view(), name='task_detail'),

    # Logs & Notifications
    path('activity-logs/', ActivityLogListView.as_view(), name='activity_logs'),
    path('notifications/', NotificationListView.as_view(), name='notification_list'),
]
