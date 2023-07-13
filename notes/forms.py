from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title' , 'text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control my-5'}),
            'text':forms.Textarea(attrs={'class':'form-control my-5'})
        }
        labels = {
            'text':'Write your text here'
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if 'django' not in title:
            raise ValidationError('we only accept notes about django')
        return title