from .models import Business, Neighborhood, Post, Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email','profile_pic', 'bio','neighbourhood']


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['title', 'image','content','timestamp']


class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)