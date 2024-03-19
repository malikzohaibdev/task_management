from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .serializers import TaskSerializer

from .tasks import send_email_task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_email_task.delay('Task Added', f'A new task "{instance.title}" has been added.', [instance.assignee.email,
                                                                                               instance.creator.email])

    def perform_update(self, serializer):
        instance = serializer.save()
        send_email_task.delay('Task Added', f'A new task "{instance.title}" has been updated.', [instance.assignee.email,
                                                                                                 instance.creator.email])

@csrf_exempt
def just_send_email(request):
    if request.method == 'POST':
        send_email_task.delay('Task Added', 'A new task has been added.', ['recipient_email_address'])
    return Response('OK')
