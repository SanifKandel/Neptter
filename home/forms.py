from .models import Post, Profile
from django import forms
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields= ['phone','address','profile_pic','cover_pic','bio','birthday','gender']

        widgets = {
        'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['description', 'pic']