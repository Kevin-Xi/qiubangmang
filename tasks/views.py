#-- coding:utf-8 --
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from models import Task
from forms import PostForm

def post(request):
	if request.user.is_authenticated():
		form=PostForm()
		if request.method=="POST":
			form=PostForm(request.POST.copy())
			if form.is_valid():
				poster=request.user.username
				title=form.cleaned_data["title"]
				content=form.cleaned_data["content"]
				bonus=form.cleaned_data["bonus"]
				post=Task(poster=poster,title=title,content=content,bonus=bonus)
				post.save()
				return HttpResponseRedirect("/")
		form=PostForm()
		return render_to_response("tasks/post.html",{'form':form,})
	return HttpResponseRedirect("/accounts/login/")

def show_task(request,no):
	if request.user.is_authenticated():
		try:
			no=int(no)
			task=Task.objects.filter(id=no).values()[0]
		#except ValueError:
		except:
			raise Http404()
		return render_to_response("tasks/showtask.html", {'task' : task, })
	return HttpResponseRedirect("/accounts/login/")

def receive(request, no):
	if request.user.is_authenticated():
		try:
			no=int(no)
			task=Task.objects.get(id=no)
		except:
			raise Http404()
		task.receiver=request.user.username
		task.save()
		return HttpResponseRedirect("/tasks/%s/" % no)
	return HttpResponseRedirect("/accounts/login/")
