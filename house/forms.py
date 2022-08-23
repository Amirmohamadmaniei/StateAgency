from django import forms

from house.models import RequestVisit


class RequestVisitForm(forms.ModelForm):
    class Meta:
        model = RequestVisit
        fields = ('phone', 'email', 'message')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }
