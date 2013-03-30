from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from forms import RegisterForm, LoginForm

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			new_user=form.save()
			_login(request, form.cleaned_data['username'], form.cleaned_data['password'])
			return HttpResponseRedirect("/accounts/welcome/")
	else:
		form=UserCreationForm()
	return render_to_response("registration/register.html", {'form':form,})

def welcome(request):
	if request.user.is_authenticated():
		return HttpResponse("Welcome, %s" % request.user.username)
	else:
		return HttpResponse("707")

def _login(request, username, password):
	ret=False
	user=authenticate(username=username, password=password)
	if user:
		if user.is_active:
			auth_login(request, user)
			ret=True
		else:
			print '1'
	else:
		print '2'
	return ret
