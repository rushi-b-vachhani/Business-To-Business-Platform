from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='accounts:SignIn')
def home(request, var_from_page=None):
	if var_from_page is not None and var_from_page != "":
		return render(request, "home/Home.html", {'from_page': var_from_page})
	
	return render(request, "home/Home.html")
