from django.shortcuts import render
from .models import Business, Neighborhood, Post, Profile
from django.contrib.auth.models import User
from .forms import NewBusinessForm, NewNeighborhoodForm, PostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


def index(request):
    neigborhoods = Neighborhood.objects.all()
    return render(request, 'index.html', {"neigborhoods": neigborhoods})


def signup(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    posts = Post.objects.filter(user=current_user.id).all
    return render(request, 'registration/profile.html', {"posts": posts})


@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    obj = get_object_or_404(Profile, user_id=id)
    obj2 = get_object_or_404(User, id=id)
    form = UpdateProfileForm(request.POST or None, request.FILES, instance=obj)
    form2 = UpdateUserForm(request.POST or None, instance=obj2)
    if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        return HttpResponseRedirect("/profile")

    return render(request, "registration/update_profile.html", {"form": form, "form2": form2})

@login_required(login_url='/accounts/login/')
def neigborhood(request):
    
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neigborhood = form.save(commit=False)
            neigborhood.admin = request.user

            neigborhood.save()

        return redirect('index')

    else:
        form = NewNeighborhoodForm()
    return render(request, 'newneighborhood.html', {"form": form})


@login_required(login_url='/accounts/login/')
def joinneigborhood(request, id):
    neigborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = neigborhood
    request.user.profile.save()
    return redirect('index') 

def leaveneigborhood(request, id):
    neigborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('index')    


@login_required(login_url='/accounts/login')
def view_neigborhood(request, id):
    neigborhood = Neighborhood.objects.get(id=id)
    biz = Business.objects.filter(business_hood=id)
    post = Post.objects.filter(neighborhood=id)

    return render(request, 'view_neigborhood.html',  {
        'neigborhood': neigborhood,'business':biz,'post': post
    })

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.user = current_user

            biz.save()

        return redirect('index')

    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {"form": form})

@login_required(login_url='/accounts/login')
def view_biz(request, id):
    biz = Business.objects.get(id=id)
    return render(request, {'business':biz,
    })

@login_required(login_url='/accounts/login/')
def search(request):
    if 'business' in request.GET and request.GET['business']:
        business = request.GET.get("business")
        results = Business.search_business(business)
        message = f'business'
        return render(request, 'search.html', {'business': results, 'message': message})
    else:
        message = "No results found, please try again"
    return render(request, 'search.html', {'message': message})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user

            post.save()

        return redirect('index')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})
