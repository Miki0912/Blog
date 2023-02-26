from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'myblogapp/home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'myblogapp/post_details.html'