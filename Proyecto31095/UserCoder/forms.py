from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import CharField

from UserCoder.models import *

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "__all__"

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'last_name')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"

class WriteMessage(forms.Form):
    message = CharField(max_length=200)