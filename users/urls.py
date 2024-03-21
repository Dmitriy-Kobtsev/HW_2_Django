from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users import apps
from users.views import RegisterView, UserConfirmEmailView, EmailConfirmedView, EmailConfirmationFailedView, \
    EmailConfirmationSentView, UserForgotPasswordView, UserPasswordResetConfirmView, UserUpdateView, gen_new_password

app_name = apps.UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('ForgotPassword/', UserForgotPasswordView.as_view(), name='ForgotPassword'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword', gen_new_password, name='genpassword'),
]