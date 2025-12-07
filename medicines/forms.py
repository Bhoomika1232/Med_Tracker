from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Medicine

class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True, help_text='Required')

    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')

class MedicineForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['name', 'dosage', 'frequency', 'notes']
        widgets={
            'notes': forms.Textarea(attrs={'rows': 3}),
        }