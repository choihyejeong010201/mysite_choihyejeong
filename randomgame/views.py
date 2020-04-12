from django.shortcuts import render,redirect
from .models import Content
from .forms import ContentForm
# Create your views here.

def home(request):
    posts = Content.objects.all
    return render(request,'randomgame/home.html',{'posts_list':posts})

def new(request):

    if request.method == 'POST' :
        form = ContentForm(request.Post, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = ContentForm()
        return render(request,'randomgame/new.html',{'form':form})
