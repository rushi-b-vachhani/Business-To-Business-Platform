# from django import forms
# from django.contrib.auth.forms import UsernameField, UserCreationForm
# from . import models
# from accountsApp.models import Profile
# from django.contrib.auth.models import User
#
#
# class mobileNumberForm(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields = ['UserMobileNumber', ]
#
# 		widgets = {
# 			'UserMobileNumber': forms.TextInput(attrs={'placeholder': 'Mobile Number', 'class': 'form-control', 'type': 'number', }, ),
# 		}
#
# 	# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-a-specific-field-attribute
# 	# https://www.youtube.com/watch?v=wVnQkKf-gHo&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=27
#
# 	def clean_UserMobileNumber(self, *args, **kwargs):
# 		mobilenumber = self.cleaned_data.get('UserMobileNumber')
# 		mob = int(Profile.objects.filter(UserMobileNumber=mobilenumber).count())
# 		# print(mob)
# 		if mob is None or mob == 0:
# 			raise forms.ValidationError("Please enter the correct registered mobile number!")
#
# 		return mobilenumber
#
# # class PlaceholderForUser(forms.ModelForm):
# # 	class Meta:
# # 		model = User
# # 		fields = ['username']
# # 		widgets = {
# # 			'username': forms.TextInput(attrs={'placeholder': 'Chagan Username Dal!'}),
# # 		}

from django import forms
from django.contrib.auth.forms import UsernameField, UserCreationForm
from . import models
from accountsApp.models import Profile
from .models import Business, SellerAddress
from django.contrib.auth.models import User
from productApp.models import Product


class mobileNumberForm(forms.Form):
	UserMobileNumber = forms.CharField(
		widget=forms.TextInput(attrs={'placeholder': 'Mobile Number', 'class': 'form-control', 'type': 'number', })
	)

	# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-a-specific-field-attribute
	# https://stackoverflow.com/questions/1202839/get-request-data-in-django-form   ----- having similar problem as mine
	# https://www.youtube.com/watch?v=wVnQkKf-gHo&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=27
	
	# https://stackoverflow.com/questions/1202839/get-request-data-in-django-form
	# the last comment is to know the current mobile number matches with "loged in" user's mobile number or not --------3
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)  # -------3
		super(mobileNumberForm, self).__init__(*args, **kwargs)
		
	def clean_UserMobileNumber(self, *args, **kwargs):
		mobilenumber = self.cleaned_data.get('UserMobileNumber')
		p = Profile.objects.filter(UserMobileNumber=mobilenumber).first()
		if len(mobilenumber) != 10:
			raise forms.ValidationError("Mobile number is not valid.")
		if p is not None:
			if self.request and (self.request.profile.UserMobileNumber != p.UserMobileNumber):
				raise forms.ValidationError("Please enter your registered mobile number.")
		else:
			raise forms.ValidationError("Please enter your registered mobile number.")
		
		return mobilenumber


class BusinessDetailsForm1(forms.ModelForm):
	
	class Meta:
		model = Profile
		
		fields = ['UserCompanyName', ]

		widgets = {
			'UserCompanyName': forms.TextInput(attrs={'class': 'form-control', }),
		}


class BusinessDetailsForm2(forms.ModelForm):
	class Meta:
		model = User
		
		fields = ['email', ]
		
		widgets = {
			'email': forms.TextInput(attrs={'class': 'form-control', }),
		}


class BusinessAddressForm(forms.ModelForm):
	class Meta:
		model = SellerAddress
		
		fields = ['SellerAddress', 'SellerAddressLocality', 'SellerAddressCity', 'SellerAddressPinCode', 'SellerAddressState', 'SellerAddressCountry', ]
		
		widgets = {
			'SellerAddress': forms.TextInput(attrs={'class': 'form-control', }),
			'SellerAddressLocality': forms.TextInput(attrs={'class': 'form-control', }),
			'SellerAddressCity': forms.TextInput(attrs={'class': 'form-control', }),
			'SellerAddressPinCode': forms.TextInput(attrs={'class': 'form-control', }),
			'SellerAddressState': forms.TextInput(attrs={'class': 'form-control', }),
			'SellerAddressCountry': forms.TextInput(attrs={'class': 'form-control', }),
		}


class AddProductForm1(forms.ModelForm):
	class Meta:
		model = Product
		
		fields = ['ProductImageUrl', 'ProductName', ]
		
		widgets = {
			'ProductImageUrl': forms.FileInput(attrs={'class': 'form-control', 'id': 'id_ProductImageUrl1',  'Name': 'name_ProductImageUrl1', }),
			'ProductName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Product Name', 'id': 'id_ProductImageUrl1', 'Name': 'name_ProductImageUrl1', }),
		}


class AddProductForm2(forms.ModelForm):
	class Meta:
		model = Product

		fields = ['ProductImageUrl', 'ProductName', ]

		widgets = {
			'ProductImageUrl': forms.FileInput(attrs={'class': 'form-control', 'id': 'id_ProductImageUrl2', 'Name': 'name_ProductImageUrl2', }),
			'ProductName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Product Name', 'id': 'id_ProductImageUrl2', 'Name': 'name_ProductImageUrl2', }),
		}


class AddProductForm3(forms.ModelForm):
	class Meta:
		model = Product

		fields = ['ProductImageUrl', 'ProductName', ]

		widgets = {
			'ProductImageUrl': forms.FileInput(attrs={'class': 'form-control', 'id': 'id_ProductImageUrl3', 'Name': 'name_ProductImageUrl3', }),
			'ProductName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Product Name', 'id': 'id_ProductImageUrl3', 'Name': 'name_ProductImageUrl3', }),
		}
