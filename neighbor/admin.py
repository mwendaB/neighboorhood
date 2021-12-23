from django.contrib import admin
from neighbor.models import Business, Neighborhood, Post, Profile

# Register your models here.

admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)