from django import forms
from .models import Conference,Submission
from django.utils import timezone
from django.core.exceptions import ValidationError
class ConferenceForm(forms.ModelForm):
    class Meta:
        model=Conference
        fields=['name','theme','location','start_date','description','end_date']
        labels={
            'name':"titre de la conférence:",
            'theme':"thematique de la conference:",
        }
        widgets={
            'name' :forms.TextInput(
                attrs={
                    'placeholder':"entrez un titre à la conference"
                    
                }
            ),
            'start_date':forms.DateInput(
                attrs ={
                    'type':"date"
                }
            ),
            'end_date':forms.DateInput(
                attrs ={
                    'type':"date"
                }
            )
            
        }
class SubmissionForm(forms.ModelForm):
    keyword = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter keywords separated by commas'}),
        help_text='Separate keywords with commas',
        required=True
    )
    
    class Meta:
        model = Submission
        fields = ['title', 'abstract', 'keyword', 'paper', 'status', 'payed', 'conference']
        widgets = {
            'abstract': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
    
    
    def clean_paper(self):
        paper = self.cleaned_data.get('paper')
    
        return paper
    def clean(self):
        cleaned_data = super().clean()
        conference = cleaned_data.get('conference')
        
        if conference and conference.start_date:
            today = timezone.now().date()
            if conference.start_date <= today:
                raise ValidationError("La soumission ne peut être faite que pour des conférences à venir.")
        
        if self.user:
            today = timezone.now().date()
            same_day_submissions = Submission.objects.filter(
                user=self.user,
                submission_date=today
            )
            
            if self.instance and self.instance.submission_id:
                same_day_submissions = same_day_submissions.exclude(submission_id=self.instance.submission_id)
                
            if same_day_submissions.count() >= 3:
                raise ValidationError("Vous ne pouvez pas soumettre à plus de 3 conférences par jour.")
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance

class SubmissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'abstract', 'keyword', 'paper']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'keyword': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mots-clés séparés par des virgules'}),
            'paper': forms.FileInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'keyword': 'Séparez les mots-clés par des virgules',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance and self.instance.submission_id:
            self.fields['title'].widget.attrs['readonly'] = False  
    
    def clean(self):
        cleaned_data = super().clean()
        
        if self.instance.status in ['accepted', 'rejected']:
            raise ValidationError("Impossible de modifier une soumission avec le statut 'accepté' ou 'rejeté'.")
        
        return cleaned_data
    
    def clean_paper(self):
        paper = self.cleaned_data.get('paper')
        
        if not paper:
            return self.instance.paper
        
        if not paper.name.lower().endswith('.pdf'):
            raise ValidationError("Le fichier doit être un PDF.")
        
        return paper