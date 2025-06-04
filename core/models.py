from django.contrib.auth.models import AbstractUser
from django.db import models


# 1. User Authentication + RBAC
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


# 3. Team & Project Management
class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, limit_choices_to={'role': 'member'})

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'})
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# 4. Task Management
class Task(models.Model):
    STATUS_CHOICES = [
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'member'})
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_do')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# 5. Activity Logs & Audit Trails
class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    model = models.CharField(max_length=50)  # e.g., 'Task', 'Project'
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} {self.action} {self.model}({self.object_id})"


# 6. Notification System (Optional Bonus)
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
    

