from django.conf.urls import url
from .views import Login, Logout, PasswordReset, PasswordResetDone, PasswordChange, Register

urlpatterns = [
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^register/', Register.as_view(), name='register'),
    url(r'^reset-password/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    url(r'^reset-password/', PasswordReset.as_view(), name='password_reset'),
    url(r'^change-password/', PasswordChange.as_view(), name='password_change'),
]
