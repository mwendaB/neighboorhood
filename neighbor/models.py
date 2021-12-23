from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    neigborhood_name = models.CharField(max_length=200)
    neigborhood_location = models.CharField(max_length=200)
    neigborhood_description = models.TextField(max_length=500, blank=True)
    neigborhood_photo = CloudinaryField('photo', default='photo')
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='admin')


    def __str__(self):
        return self.neigborhood_name

    def save_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()    

    def update_neighborhood(self):
        neigborhood_name = self.neigborhood_name
        self.neigborhood_name = neigborhood_name    

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        return cls.objects.filter(id=neigborhood_id)

    @property
    def occupants_count(self):
        return self.neighbourhood_users.count() 
