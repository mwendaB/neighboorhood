from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name = 'index'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('joinneigborhood/<id>', views.joinneigborhood, name='joinneigborhood'),
    path('leavehood/<id>', views.leaveneigborhood, name='leaveneigborhood'),
    path('update/<id>', views.update_profile, name='update_profile'),
    path('hood_info/(?P<id>\d+)', views.view_neigborhood, name='view_hood'),
    path('new_business/', views.new_business, name='new_business'),
    path('newhood/', views.neigborhood, name='hood'),
    path('new_post', views.new_post, name='post'),  

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)