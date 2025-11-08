from django.urls import path
from . import views
from .views import *
urlpatterns = [
    #path("liste/",views.list_conferences,name="liste_conferences")
    path("liste/", ConferenceList.as_view(), name="liste_conferences"),
    path("<int:pk>/", ConferenceDetails.as_view(), name="conference_details"),
    path("add/", ConferenceCreate.as_view(),name="Conference_creation"),
    path("edit/<int:pk>/", ConferenceUpdate.as_view(),name="Conference_update"),
    path("delete/<int:pk>/", ConferenceDelete.as_view(),name="Conference_delete"),
    path('submissions/', views.list_submissions, name='list_submissions'),
    path('conferences/submission/<str:pk>/', submission_details.as_view(), name='submission_details'),
    path('download/<str:submission_id>/', views.download_paper, name='download_paper'),
    path('add_submission/', SubmissionCreate.as_view(),name="Submission_creation"),
    path('submissions/update/<str:pk>/', UpdateSubmission.as_view(), name='update_submission'),
]