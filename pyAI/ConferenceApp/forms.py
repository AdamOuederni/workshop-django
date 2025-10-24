from django import forms
from .models import Conference
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
