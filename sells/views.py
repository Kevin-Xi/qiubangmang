#-- coding:utf-8 --
import datetime
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from models import Ability
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
				post = Ability(abilityNAME=title, abilityDESCRIBE=content,
						logDATE=datetime.datetime.now(),rpREQUIRED=bonus, abilityRAISER=poster)
				post.save()
				return HttpResponseRedirect("/")
		form=PostForm()
		return render_to_response("sells/post.html",{'form':form,})
	return HttpResponseRedirect("/accounts/login/")

def show_ability(request,no):
	if request.user.is_authenticated():
		if request.method == 'POST':
			receive(request, no)
			return HttpResponseRedirect("/sells/%s/" % no)
		else:
			try:
				no=int(no)
				sell=Ability.objects.get(id=no)
			except:
				raise Http404()
			return render_to_response("sells/showability.html", {'sell' : sell, })
	return HttpResponseRedirect("/accounts/login/")

def receive(request, no):
	sell = Ability.objects.get(id=no)

	if not sell.abilityRECEIVER:
		sell.abilityRECEIVER = request.user
		sell.adoptDATE = datetime.datetime.now()
		sell.save()
