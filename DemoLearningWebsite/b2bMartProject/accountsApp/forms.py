from django import forms
from django.contrib.auth.forms import UsernameField, UserCreationForm
from . import models
from django.contrib.auth.models import User


class ProfileFormCreation(forms.ModelForm):
	class Meta:
		model = models.Profile
		fields = ['UserProfilePictureUrl', 'UserMobileNumber', 'UserAltMobileNumber', 'UserCompanyName', 'UserCompanyYear', ]

		widgets = {
			'UserMobileNumber': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
			'UserAltMobileNumber': forms.TextInput(attrs={'placeholder': 'Alternate Mobile Number'}),
			'UserCompanyName': forms.TextInput(attrs={'placeholder': 'Company Name'}),
			'UserCompanyYear': forms.TextInput(attrs={'placeholder': 'Company Year'}),
		}

# class PlaceholderForUser(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ['username']
# 		widgets = {
# 			'username': forms.TextInput(attrs={'placeholder': 'Chagan Username Dal!'}),
# 		}