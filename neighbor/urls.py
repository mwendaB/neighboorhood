from django.urls import re_path,path,include
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
  
  path('accounts/register/',views.register,name='register'),
  path('accounts/login/',views.login,name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
  path('',views.index, name='index'),
  path('new-hood/', views.create_neighbourhood, name='new-hood'),
  path('join_hood/<id>', views.join_neighbourhood, name='join-hood'),
  path('leave_hood/<id>', views.leave_neighbourhood, name='leave-hood'),
  path('single_hood/<hood_id>', views.single_neighbourhood, name='single-hood'),
  path('<hood_id>/new-post', views.create_post, name='post'),
]
