from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile,Link

# Create your views here.
class LinkListView(ListView):
    model = Link
    # will look for a template file with model_list.html -> link_list.html., prefix(link from Link model)


