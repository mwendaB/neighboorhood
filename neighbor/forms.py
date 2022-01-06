from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighbourhood, Profile, Post, Business
from django.forms.widgets import Textarea

    
class Registration(UserCreationForm):
    email = forms.EmailField()

class Meta:
    model = User
    fields = ['username','email','password1','password2']



class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'neighbourhood','profile_pic', 'bio', 'phone_number']
        
        widgets = {
            'bio': Textarea(attrs={'cols': 20, 'rows': 5}),
        }
class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')