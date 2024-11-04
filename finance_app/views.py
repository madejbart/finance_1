from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Profile, Company
# Create your views here.

def index(request):
    """The home page for finance."""
    return render(request, 'index.html')
class ProfilesView(ListView):
    model = Profile
    context_object_name = "profiles"
    template_name = "profiles.html"

