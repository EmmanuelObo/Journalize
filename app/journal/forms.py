from django import forms
from .models import Journal


class JournalForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title','class':'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'What\'s on your mind today?','style':'height:250px;margin-bottom: 30px;','class':'form-control'}))
    image = forms.ImageField(required=False)