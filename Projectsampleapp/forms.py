from django import forms
from Projectsampleapp.models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        # fields="Name,Age"
        # exclude="Age"  --to exclide certain field--

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields="__all__"