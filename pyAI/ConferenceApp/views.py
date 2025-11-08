from django.shortcuts import render
from .models import Conference,Submission
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ConferenceForm,SubmissionForm,SubmissionUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
import os
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
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
class ConferenceCreate(LoginRequiredMixin,CreateView):
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
def list_submissions(request):
    submissions = Submission.objects.filter(user=request.user)
    return render(request, 'conferences/list_submissions.html', {'submissions': submissions})
class submission_details(DetailView):
    model=Submission
    context_object_name="submission"
    template_name="conferences/details_submission.html"


def download_paper(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    if not submission.paper:
        raise Http404("Aucun fichier trouvé.")

    file_path = submission.paper.path
    file_name = os.path.basename(file_path)
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
    return response
class SubmissionCreate(LoginRequiredMixin, CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = "conferences/form_submission.html"
    success_url = reverse_lazy("list_submissions")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
class UpdateSubmission(LoginRequiredMixin, UpdateView):
    model = Submission
    form_class = SubmissionUpdateForm
    template_name = "conferences/update_submission.html"
    
    def get_success_url(self):
        return reverse_lazy("list_submissions")
    
    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)
    
    def dispatch(self, request, *args, **kwargs):
        submission = self.get_object()
        
        if submission.status in ['accepted', 'rejected']:
            messages.error(request, "Une soumission avec l'état 'accepté' ou 'rejeté' ne peut pas être modifiée.")
            return redirect("list_submissions")
    
        if submission.user != request.user:
            raise PermissionDenied("Vous n'avez pas la permission de modifier cette soumission.")
        
        return super().dispatch(request, *args, **kwargs)
