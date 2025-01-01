from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView , DetailView , CreateView
from .models import Post
# Create your views here.


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request , 'blog/home.html' , context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title' , 'content']

def about(request):
 
    return render(request , 'blog/about.html' )