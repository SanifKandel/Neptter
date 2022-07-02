from .models import Post, Profile , Comment
from django import forms

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields= ['phone','address','profile_pic','cover_pic','bio','birthday','gender']

        widgets = {
        'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'phone': forms.NumberInput(attrs={'class': 'form-control', 'type': 'tel'}),
        'address': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
        'bio': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
        'gender': forms.Select(attrs={'class': 'form-control','id': 'gender'}),
        'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
        'cover_pic': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
        

        }

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['description', 'pic']

class NewCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['body']