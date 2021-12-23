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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idNo = models.IntegerField(default=0)
    email = models.CharField(max_length=30, blank=True)
    profile_pic = CloudinaryField('profile')
    bio = models.TextField(max_length=500, blank=True)
    neighbourhood = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    image = CloudinaryField('images')
    content = models.TextField(max_length=300, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    neighbourhood = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, default='', null=True, blank=True)

    def __str__(self):
        return self.title

    def save_post(self):
        return self.save()

    def delete_post(self):
        self.delete()



