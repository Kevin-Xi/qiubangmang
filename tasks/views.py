#-- coding:utf-8 --
import datetime
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from models import Mission
from forms import PostForm

def post(request):
	if request.user.is_authenticated():
		form=PostForm()
		if request.method=="POST":
			form=PostForm(request.POST.copy())
			if form.valid():
				poster=request.user
				title=form.cleaned_data["title"]
				content=form.cleaned_data["content"]
				bonus=form.cleaned_data["bonus"]
				deadline = form.cleaned_data["deadline"]
				post = Mission(missionNAME=title, missionDESCRIBE=content,
						logDATE=datetime.datetime.now(), deadline=deadline,
						rpBONUS=bonus, missionRAISER=poster)
				post.save()
				return HttpResponseRedirect("/")
		form=PostForm()
		return render_to_response("tasks/post.html",{'form':form,})
	return HttpResponseRedirect("/accounts/login/")

def show_task(request,no):
	if request.user.is_authenticated():
		if request.method == 'POST':
			receive(request, no)
			return HttpResponseRedirect("/tasks/%s/" % no)
		else:
			try:
				no=int(no)
				task=Mission.objects.get(id=no)
			except:
				raise Http404()
			return render_to_response("tasks/showtask.html", {'task':task, })
	return HttpResponseRedirect("/accounts/login/")

def receive(request, no):
	task = Mission.objects.get(id=no)

	if not task.missionRECEIVER:
		task.missionRECEIVER = request.user
		task.acceptDATE = datetime.datetime.now()
		task.save()
