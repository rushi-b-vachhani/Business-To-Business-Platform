from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse

@login_required(login_url="accounts:SignIn")
def index(request):
    return render(request,'UserLogin.html',{'name':'Rushi'})
