from django.contrib import admin
from django.urls import path, include

from users.views import CustomTokenObtainPairView
from tasks.views import just_send_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', CustomTokenObtainPairView.as_view()),
    path('api/user/', include('users.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('send-email/', just_send_email)

]
