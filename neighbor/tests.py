import datetime
from .views import profile
from .models import Business, Neighbourhood, Post, Profile 
from django.contrib.auth.models import User
from django.test import TestCase

class ProfileTest(TestCase):
    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.neighbourhood =  Neighbourhood(hood_name = "Nakuru", location= "Milimani", admin = self.user,description='nyumbakumi', profile_pic="myhood.jpg")
        self.neighbourhood.save()
        self.profile = Profile(email='info@g.com', profile_pic='profile.jpg', bio='profile',neighbourhood=self.neighbourhood,
                                    user=self.user)
      
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        testsaved = Profile.objects.all()
        self.assertFalse(len(testsaved) > 0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)


class NeighbourhoodTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.neighbourhood =  Neighbourhood(hood_name = "Nakuru", hood_location= "Milimani", admin = self.user,hood_description='nyumbakumi', hood_photo="myhood.jpg")
        self.neighbourhood.save()
   
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save_hood(self):
        self.neighbourhood.save_hood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_hood(self):
        self.neighbourhood.delete_hood()
        testsaved = Neighbourhood.objects.all()
        self.assertFalse(len(testsaved) > 0)

    # def test_occupants_count(self):

class BusinessTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.neighbourhood =  Neighbourhood(hood_name = "Nakuru", hood_location= "Milimani", admin = self.user,hood_description='nyumbakumi')
        self.neighbourhood.save()
        self.biz = Business(user=self.user,business_name="Sneakers", neighborhood=self.neighbourhood,business_email="sneakers@gmail.com", business_desc="Selling sneakers")
        self.biz.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.biz,Business))

    def test_save_business(self):
        self.biz.save_business()
        biz = Business.objects.all()
        self.assertTrue(len(biz) > 0)

    def test_delete_hood(self):
        self.biz.delete_business()
        biz = Business.objects.all()
        self.assertFalse(len(biz) > 0)

class PostTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.neighbourhood =  Neighbourhood(hood_name = "Nakuru", hood_location= "Milimani", admin = self.user,hood_description='nyumbakumi', hood_photo="myhood.jpg")
        self.neighbourhood.save()
        self.post = Post(user=self.user,title="Sneakers",image="post.jpg" ,content ="my post", timestamp=datetime.datetime,neighbourhood=self.neighbourhood)
        self.post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.objects.all()
        self.assertFalse(len(post) > 0)