from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
#from forms import RegisterForm, LoginForm
#from forms import LoginForm
from django.template import RequestContext

def post(request):
	# form, auth, database, show
	return None
