from django.urls import path
from . import views
from .views import *
urlpatterns = [
    #path("liste/",views.list_conferences,name="liste_conferences")
    path("liste/", SessionList.as_view(), name="liste_sessions"),
    path("details/<int:pk>/", SessionDetails.as_view(), name="session_details"),
    path("add/",SessionCreate.as_view(),name="session_add")

    
]