from django import forms
from home import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        exclude = ('id',)
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'sub': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }
