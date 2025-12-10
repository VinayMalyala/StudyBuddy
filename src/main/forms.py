from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Room
from .widgets import CustomPictureWidget


class UserForm(forms.ModelForm):
    avatar = forms.ImageField(widget=CustomPictureWidget)
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio' ]

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
