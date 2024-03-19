from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, just_send_email

router = DefaultRouter()
router.register('', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send-email/', just_send_email),
]
