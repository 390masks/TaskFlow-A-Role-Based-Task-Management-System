from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task, Project, Team, User, ActivityLog, Notification

# Helper function to create activity log
def create_activity_log(user, action, model_name, obj_id, details=""):
    if user:  # prevent null user error
        ActivityLog.objects.create(
            user=user,
            action=action,
            model=model_name,
            object_id=obj_id,
            details=details
        )


# Task signals

@receiver(post_save, sender=Task)
def log_task_save(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    # NOTE: This is a placeholder; ideally use request.user from view
    user = instance.assigned_to

    details = f"Task '{instance.title}' was {'created' if created else 'updated'}."
    create_activity_log(user, action, 'Task', instance.id, details)

    # Create notification
    Notification.objects.create(
        user=instance.assigned_to,
        message=f"Task '{instance.title}' has been {'assigned to you' if created else 'updated'}."
    )

@receiver(post_delete, sender=Task)
def log_task_delete(sender, instance, **kwargs):
    user = instance.assigned_to
    details = f"Task '{instance.title}' was deleted."
    create_activity_log(user, 'delete', 'Task', instance.id, details)

    # Optional: Notification on task delete
    Notification.objects.create(
        user=instance.assigned_to,
        message=f"Task '{instance.title}' has been deleted."
    )


# Project signals

@receiver(post_save, sender=Project)
def log_project_save(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    user = instance.created_by
    details = f"Project '{instance.name}' was {'created' if created else 'updated'}."
    create_activity_log(user, action, 'Project', instance.id, details)

@receiver(post_delete, sender=Project)
def log_project_delete(sender, instance, **kwargs):
    user = instance.created_by
    details = f"Project '{instance.name}' was deleted."
    create_activity_log(user, 'delete', 'Project', instance.id, details)


# Team signals

@receiver(post_save, sender=Team)
def log_team_save(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    user = instance.members.first()  # Might be None
    details = f"Team '{instance.name}' was {action}d."
    create_activity_log(user, action, 'Team', instance.id, details)

@receiver(post_delete, sender=Team)
def log_team_delete(sender, instance, **kwargs):
    user = instance.members.first()  # Might be None
    details = f"Team '{instance.name}' was deleted."
    create_activity_log(user, 'delete', 'Team', instance.id, details)


# User signals

@receiver(post_save, sender=User)
def log_user_save(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    details = f"User '{instance.username}' was {action}d."
    create_activity_log(instance, action, 'User', instance.id, details)

@receiver(post_delete, sender=User)
def log_user_delete(sender, instance, **kwargs):
    details = f"User '{instance.username}' was deleted."
    create_activity_log(instance, 'delete', 'User', instance.id, details)
