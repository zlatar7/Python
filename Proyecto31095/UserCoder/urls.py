from django.urls import path
from django.contrib.auth.views import LogoutView

from UserCoder.views import *

urlpatterns = [
    path('login', login_request, name='UserCoderLogin'),
    path('register', register , name='UserCoderRegister'),
    path('logout', LogoutView.as_view(template_name='UserCoder/logout.html'), name='UserCoderLogout')
]