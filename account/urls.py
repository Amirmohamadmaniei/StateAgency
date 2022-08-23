from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.LogoutRedirectView.as_view(), name='logout'),
    path('profile/edit/<int:pk>', views.EditProfileView.as_view(), name='edit_profile'),
]
