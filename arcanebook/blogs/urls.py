from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home,name='homePage'),
    path('new-post',views.new_post,name='newPost'),
    path('new-post-upload',views.upload_new_post,name='upload new post'),
    path('post/<slug>',views.post,name='Full Post'),
    path('profile',views.profile,name='user profile'),
]

