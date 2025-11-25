from django.shortcuts import render
from .models import Session
from django.views.generic import ListView,DetailView,CreateView
from .forms import SessionForm
from django.urls import reverse_lazy
class SessionList(ListView):
    model=Session
    context_object_name="liste"
    template_name="conferences/liste_sessions.html"
# Create your views here.
class SessionDetails(DetailView):
    model=Session
    context_object_name="Session"
    template_name="conferences/details_session.html"
class SessionCreate(CreateView):
    model=Session
    template_name="conferences/form_session.html"
    # fields="__all__"
    form_class=SessionForm
    success_url=reverse_lazy("liste_sessions")