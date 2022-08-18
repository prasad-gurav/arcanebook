from dataclasses import field
from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from tkinter.tix import Tree
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

from .utils import slug_generator


# Create your models here.
class BlogModel(models.Model,):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    discription = models.CharField(max_length=1000,null=True,blank=True)
    content = FroalaField()
    slug = models.SlugField(max_length=1000,null=True,blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True) # when blogs are created.
    updated_at = models.DateTimeField(auto_now=True) # when blogs are updated. 

    def __str__(self):
        return self.title

    # save method for overide slug field 
    def save(self,*args,**kwargs):
        self.slug = slug_generator(self.title)
        super(BlogModel,self).save(*args,**kwargs)



class profile(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    profilePic = models.ImageField(upload_to='profile',null=True,blank=True)
    proffesion = models.CharField(max_length=100,null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    # social links 
    instagram = models.TextField(null=True,blank=True)
    twitter = models.TextField(null=True,blank=True)
    linkedin = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)