from .models import Profile 
from django import forms

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields= ['phone','address','profile_pic','cover_pic','bio','birthday','gender']

        widgets = {
        'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date' }),
        'phone': forms.NumberInput(attrs={'class': 'form-control', 'type': 'tel','placeholder':'Enter Your Phone No. here'}),
        'address': forms.TextInput(attrs={'class': 'form-control', 'type': 'text','placeholder':'Enter Your Address here'}),
        'bio': forms.TextInput(attrs={'class': 'form-control', 'type': 'text','placeholder':'Enter Your Bio here'}),
        'gender': forms.Select(attrs={'class': 'form-control','id': 'gender','placeholder':'Enter Your Gender here'}),
        'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'type': 'file','placeholder':'Put Your Profile Pic here'}),
        'cover_pic': forms.FileInput(attrs={'class': 'form-control', 'type': 'file','placeholder':'Put Your Cover Pic here'}),
        

        }
