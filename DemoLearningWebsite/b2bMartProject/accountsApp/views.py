from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import forms
from django.views.decorators.csrf import csrf_protect
# Create your views here.


def signup_view(request):
	if request.user.is_authenticated:
		return redirect('homeAppUrls:fromPage', var_from_page='You are already Signed Up')
	else:
		if request.method == 'POST':
			form = forms.UserCreationForm(request.POST)
			if form.is_valid():
				user = form.save()  # returns user object
				login(request, user)  # login the user
				return redirect('accounts:ProfileDetail')
		else:
			form = forms.UserCreationForm()
		
		return render(request, 'accounts/SignUp.html', {'form': form})


@login_required(login_url='accounts:SignIn')
def create_profile_view(request):
	if request.method == 'POST':
		profile_form = forms.ProfileFormCreation(request.POST)
		if profile_form.is_valid():
			inst = profile_form.save(commit=False)
			inst.user = request.user
			inst.save()
			return redirect('homeAppUrls:home')
	else:
		profile_form = forms.ProfileFormCreation()

	return render(request, 'accounts/ProfileDetail.html', {'profileForm': profile_form})


def signin_view(request):
	if request.user.is_authenticated:
		return redirect('homeAppUrls:fromPage', var_from_page='You are already Signed In')
	else:
		if request.method == 'POST':
			form = AuthenticationForm(data=request.POST)
			if form.is_valid():
				user = form.get_user()
				login(request, user)
				if 'next' in request.POST:
					# print(request.POST.get('next') + "1")
					return redirect(request.POST.get('next'))
				else:
					# print(request.POST.get('next') + "2")
					return redirect('homeAppUrls:home')
		else:
			form = AuthenticationForm()
		
		return render(request, 'accounts/SignIn.html', {'form': form})
	

def logout_view(request):
	#if request.method == 'POST':
		logout(request)
		return redirect('accounts:SignIn')

