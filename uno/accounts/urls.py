from django.urls import path

from .views import (
    SignUpView,
    EmailConformationView,
    LoginView,
    PasswordResetApiView,
    LogOutView,
)


urlpatterns = [
    path(
        'signup/',
        SignUpView.as_view(),
        name='signup',
    ),
    path(
        'email-conformation/<str:activation_key>/',
        EmailConformationView.as_view(),
        name='email_conformation'
    ),
    path('login/', 
        LoginView.as_view(),
        name='login_view'
    ),
    path(
        'change-password/',
        PasswordResetApiView.as_view(),
        name='change-password',
    ),
    path('logout/', 
        LogOutView.as_view()
    ),
]
