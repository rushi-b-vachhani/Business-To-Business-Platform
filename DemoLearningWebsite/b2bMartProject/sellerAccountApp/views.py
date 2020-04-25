from _lsprof import profiler_entry

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import forms
from sellerAccountApp.models import Seller
# Create your views here.

# app_name = 'sellerAccountUrls'


@login_required(login_url='accounts:SignIn')
def register_seller(request):
	# if request.user.is_authenticated:
	
	if request.method == 'POST':
		form = forms.mobileNumberForm(request.POST or None, request=request.user or None, )
		if form.is_valid():
			form1 = forms.BusinessDetailsForm1(instance=request.user.profile)
			form2 = forms.BusinessDetailsForm2(instance=request.user)
			return render(request, 'sellerAccounts/RegisterSeller.html', {'BusinessDetailsForm1': form1, 'BusinessDetailsForm2': form2,})
	else:
		form = forms.mobileNumberForm()
		
	return render(request, 'sellerAccounts/RegisterSeller.html', {'mobileNumberForm': form, })


@login_required(login_url='accounts:SignIn')
def register_business_details(request):
	# if request.user.is_authenticated:
	print("Rushi")
	if request.method == 'POST':
		# https://stackoverflow.com/questions/4673985/how-to-update-an-object-from-edit-form-in-django -- REFER
		# https://www.youtube.com/watch?v=no99-sgCqOo&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=28 -- REFER
		
		# for editing specific object
		form1 = forms.BusinessDetailsForm1(request.POST or None, instance=request.user.profile)
		form2 = forms.BusinessDetailsForm2(request.POST or None, instance=request.user)
		if form1.is_valid() and form2.is_valid():
			form1.save()
			form2.save()
			f1 = forms.AddProductForm1(prefix="form1")
			f2 = forms.AddProductForm2(prefix="form2")
			f3 = forms.AddProductForm3(prefix="form3")
			return render(request, 'sellerAccounts/RegisterSeller.html', {'AddProductForm1': f1, 'AddProductForm2': f2, 'AddProductForm3': f3, })
		else:
			return render(request, 'sellerAccounts/RegisterSeller.html', {'BusinessDetailsForm1': form1, 'BusinessDetailsForm2': form2, })
	else:
		form = forms.mobileNumberForm()
	return render(request, 'sellerAccounts/RegisterSeller.html', {'mobileNumberForm': form, })
	
	
@login_required(login_url='accounts:SignIn')
def register_products(request):
	# if request.user.is_authenticated:
	if request.method == 'POST':
		f1 = forms.AddProductForm1(request.POST or None, request.FILES, prefix="form1")
		f2 = forms.AddProductForm2(request.POST or None, request.FILES, prefix="form2")
		f3 = forms.AddProductForm3(request.POST or None, request.FILES, prefix="form3")
		if f1.is_valid() and f2.is_valid() and f3.is_valid():
			# https://stackoverflow.com/questions/18489393/django-submit-two-different-forms-with-one-submit-button
			# ----- Real Answer that how to submit multiple sorm at singlee submit button just add prefix="from1"
			
			# https://stackoverflow.com/questions/27996398/handle-multiple-modelforms-in-one-html-form
			# https://stackoverflow.com/questions/15124567/how-do-i-submit-multiple-forms-with-a-single-submit-button-in-django
			fo1 = f1.save(commit=False)
			fo2 = f2.save(commit=False)
			fo3 = f3.save(commit=False)
			# https://stackoverflow.com/questions/8632087/setting-user-id-when-saving-in-view-django
			s = Seller.objects.create(Profile=request.user.profile)
			fo1.Seller = s
			fo2.Seller = s
			fo3.Seller = s
			fo1.save()
			fo2.save()
			fo3.save()
			form = forms.BusinessAddressForm(prefix="form1")
			return render(request, 'sellerAccounts/RegisterSeller.html', {'BusinessAddressForm': form, })
		else:
			return render(request, 'sellerAccounts/RegisterSeller.html', {'AddProductForm1': f1, 'AddProductForm2': f2, 'AddProductForm3': f3, })
	else:
		form = forms.mobileNumberForm()
	
	return render(request, 'sellerAccounts/RegisterSeller.html', {'mobileNumberForm': form, })


@login_required(login_url='accounts:SignIn')
def register_seller_address(request):
	# if request.user.is_authenticated:
	# https://stackoverflow.com/questions/8632087/setting-user-id-when-saving-in-view-django
	if request.method == 'POST':
		form1 = forms.BusinessAddressForm(request.POST or None, prefix="form1")
		if form1.is_valid():
			inst = form1.save(commit=False)
			inst.Seller = request.user.profile.seller
			inst.save()
			return redirect('homeAppUrls:home')
		else:
			return render(request, 'sellerAccounts/RegisterSeller.html', {'BusinessAddressForm': form1, })
	else:
		form = forms.mobileNumberForm()
	
	return render(request, 'sellerAccounts/RegisterSeller.html', {'mobileNumberForm': form, })
