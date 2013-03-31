from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
#from forms import RegisterForm, LoginForm
from forms import LoginForm
from django.template import RequestContext

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			new_user=form.save()
			_login(request, form.cleaned_data['username'], form.cleaned_data['password1'])
			return HttpResponseRedirect("/accounts/welcome/")
	else:
		form=UserCreationForm()
	return render_to_response("accounts/register.html", {'form':form,})

def login(request):
	template_var={}
	form=LoginForm()
	if request.method=="POST":
		form=LoginForm(request.POST.copy())
		if form.is_valid():
			_login(request,form.cleaned_data['username'],form.cleaned_data['password'])
			return HttpResponseRedirect("/accounts/welcome/")
	template_var['form']=form
	return render_to_response("accounts/login.html",template_var,context_instance=RequestContext(request))

def welcome(request):
	if request.user.is_authenticated():
		#return HttpResponse("<a href='/'> Welcome, %s </a>" % request.user.username)
		#return render_to_response('index.html', {'request': request,})
		return HttpResponseRedirect("/")
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

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect("/")
