
from django import forms
from .models import Session
from django.utils import timezone
from django.core.exceptions import ValidationError
class SessionForm(forms.ModelForm):
    class Meta:
        model=Session
        fields=['title','topic','session_day','start_time']
        labels={
            'title':"titre de la session:",
            'topic':"sujet de la session:",
        }
        widgets={
            'title' :forms.TextInput(
                attrs={
                    'placeholder':"entrez un titre à la session"
                    
                }
            ),
         
        'session_day':forms.DateInput(
                attrs ={
                    'type':"date"
                }
            ),
        }