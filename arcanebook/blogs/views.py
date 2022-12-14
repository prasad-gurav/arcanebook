from http.client import HTTPResponse
from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import BlogModel
from .models import profile as myprofile
from django.contrib.auth.models import User
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs = BlogModel.objects.all().order_by('-pk')

    return render(request,"base.html",{'blogs':blogs})

def post(request,slug):
    try:
        post = BlogModel.objects.filter(slug=slug).first()
    except Exception as e:
        print(e)
    return render(request,'post.html',{'post':post})

def new_post(request):
    context = {'form':BlogForm}
    return render(request,"new_post.html",context)

def upload_new_post(request):
    try:
        if request.method == "POST":
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get("blog-title")
            disc = request.POST.get("discription")
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']
            blog_obj = BlogModel.objects.create(user=user,title=title,image=image,content=content,discription=disc)
            print(blog_obj)
    except Exception as e:
        print(e)       
    return redirect('/')


def profile(request):
    if request.user is not None:
        user_profile = myprofile.objects.filter(user=request.user).first()
        blogs = BlogModel.objects.filter(user=request.user)
        context = {'profile':user_profile,
                    'post':blogs}
    else:
        print("Login First")
        return HTTPResponse("You Need to login first.")
    return render(request,'profile.html',context)