from django import forms
from .models import destination, post_blogs


class destinationForm(forms.ModelForm):
    class Meta:
        model = destination
        fields = ['title', 'msg', 'pic', 'fee']


class post_blogsForm(forms.ModelForm):
    class Meta:
        model = post_blogs
        fields = "__all__"

        labels = {
            'Name': '',
            'Date': '',
            'Title': '',
            'Image': '',
            'Description': ''
        }

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'Date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YY'}),
            'Title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'Image': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Choose image'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your memories'})

        }
