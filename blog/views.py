from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

from .models import Posty

class BlogListView(ListView):
    model = Posty
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Posty
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
	model = Posty
	template_name = 'post_new.html'
	fields = '__all__'

class BlogUpdateView(UpdateView):
	model = Posty
	template_name= 'post_edit.html'
	fields = ['title', 'body']

class BlogDeleteView(DeleteView):
	model = Posty
	template_name= 'post_delete.html'
	success_url = reverse_lazy('home')
