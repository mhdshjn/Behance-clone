from django.urls import path
from . import views

urlpatterns = [
    path('', views.userAccount, name='profile'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('edit-account', views.editAccount, name='edit-account'),
    path('profile/<str:pk>/', views.profile, name='other_profile'),
    path('inbox/', views.inbox, name='inbox')
    ]