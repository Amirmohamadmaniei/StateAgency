from django import forms
from . import models


class CommentForm(forms.ModelForm):
    # pattern = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = models.Comment
        fields = ('description',)
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment *'})
        }
