# urls.py
from django.urls import path
from .views import CreateUserView, UserListView, UserDetailsView, CurrentUserView, LogoutView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='create_user'),
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailsView.as_view(), name='user_details'),
    path('current-user/', CurrentUserView.as_view(), name='current_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
