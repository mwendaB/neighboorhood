from django.shortcuts import render
from .models import Business, Neighborhood, Post, Profile
from django.contrib.auth.models import User
from .forms import NewBusinessForm, NewHoodForm, PostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authentica


def index(request):
  
    neigborhoods = Neighborhood.objects.all()
    return render(request, 'index.html', {"neigborhoods": neigborhoods})