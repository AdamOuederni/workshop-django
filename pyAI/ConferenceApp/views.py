from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ConferenceForm

# Create your views here.
def list_conferences(request):
    Conferences_list=Conference.objects.all()
    return render(request,"Templates/conferences/liste.html",{"liste":Conferences_list})
class ConferenceList(ListView):
    model=Conference
    context_object_name="liste"
    template_name="conferences/liste.html"
class ConferenceDetails(DetailView):
    model=Conference
    context_object_name="conference"
    template_name="conferences/details.html"
class ConferenceCreate(CreateView):
    model=Conference
    template_name="conferences/form.html"
    # fields="__all__"
    form_class=ConferenceForm
    success_url=reverse_lazy("liste_conferences")
class ConferenceUpdate(UpdateView):
    model=Conference
    template_name="conferences/form.html"
    # fields="__all__"
    success_url=reverse_lazy("liste_conferences")
    form_class=ConferenceForm
class ConferenceDelete(DeleteView):
    model=Conference
    template_name="conferences/conference_confirm_delete.html"
    success_url=reverse_lazy("liste_conferences")