from django.urls import path, include
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login')
    # path('login/', views_auth.LoginView.as_view(), name='login'),
    # path('logout/', views_auth.LogoutView.as_view(), name='logout'),
    #
    # path('password-change/', views_auth.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', views_auth.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #

    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]
