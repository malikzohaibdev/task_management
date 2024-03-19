# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .tasks import send_email_task


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, created, **kwargs):
    if created:
        # If a new task is created, trigger the Celery task asynchronously
        send_email_task.delay(instance.id)
