from .models import Profile
from django import forms
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields= ['phone','address','profile_pic','birthday','gender']

        widgets = {
        'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }