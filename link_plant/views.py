from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile,Link

# Create your views here.
class LinkListView(ListView):
    model = Link
    # will look for a template file with model_list.html -> link_list.html., prefix(link from Link model)

class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')
    # expects a  template model_form -> link_form.html


class LinkUpdateView(UpdateView):
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')
    # expects a  template model_form -> link_form.html

class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')
    # expect a template name model_confim_delete.html -> link_confirm_delete.html

def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }

    return render(request, 'link_plant/profile.html', context)
