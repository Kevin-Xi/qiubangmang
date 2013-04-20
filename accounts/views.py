from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
#from forms import RegisterForm, LoginForm
from forms import LoginForm
from django.template import RequestContext
from tasks.models import Task
from sells.models import Ability

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			new_user=form.save()
			_login(request, form.cleaned_data['username'], form.cleaned_data['password1'])
			return HttpResponseRedirect("/accounts/welcome/")
			#return HttpResponseRedirect(request.get_full_path())
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
			#return HttpResponseRedirect(url)
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

def homepage(request, username):
	if request.user.is_authenticated():
		try:
			user=User.objects.get(username=username)
		except:
			raise Http404()
		received_tasks=Task.objects.filter(poster=username).exclude(receiver="")
		unreceived_tasks=Task.objects.filter(poster=username, receiver="")
		received_abilities=Ability.objects.filter(poster=username).exclude(receiver="")
		unreceived_abilities=Ability.objects.filter(poster=username, receiver="")
		return render_to_response("accounts/homepage.html", {'request': request, 'user': user, 'received_tasks': received_tasks, 'unreceived_tasks': unreceived_tasks, 'received_abilities': received_abilities, 'unreceived_abilities': unreceived_abilities, })
	return HttpResponseRedirect("/accounts/login/")
