#-- coding:utf-8 --
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from models import Ability
from forms import PostForm

def post(request):
	if request.user.is_authenticated():
		form=PostForm()
		if request.method=="POST":
			form=PostForm(request.POST.copy())
			if form.valid():
				poster=request.user.username
				title=form.cleaned_data["title"]
				content=form.cleaned_data["content"]
				bonus=form.cleaned_data["bonus"]
				post=Ability(poster=poster,title=title,content=content,bonus=bonus)
				post.save()
				return HttpResponseRedirect("/")
		form=PostForm()
		return render_to_response("sells/post.html",{'form':form,})
	return HttpResponseRedirect("/accounts/login/")

def show_ability(request,no):
	if request.user.is_authenticated():
		try:
			no=int(no)
			sell=Ability.objects.get(id=no)
		#except ValueError:
		except:
			raise Http404()
		return render_to_response("sells/showability.html", {'sell' : sell, })
	return HttpResponseRedirect("/accounts/login/")

def receive(request, no):
	if request.user.is_authenticated():
		try:
			no=int(no)
			sell=Ability.objects.get(id=no)
		except:
			raise Http404()
		if not sell.receiver:
			sell.receiver=request.user.username
			sell.save()
		return HttpResponseRedirect("/sells/%s/" % no)
	return HttpResponseRedirect("/accounts/login/")
