from django import forms
from .models import Tasks

class InputForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['task','last_date','dead_line']
