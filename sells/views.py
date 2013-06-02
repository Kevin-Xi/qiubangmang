#-- coding:utf-8 --#
'''Process all request relatived to sells

include post and show page'''

import datetime
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from models import Ability
from forms import PostForm
from reply.forms import ReplyForm
from reply.models import Reply
from accounts.models import UserProfile

def post(request):
	'''process post page

	judge user's authenticate status and save valid post'''

	if request.user.is_authenticated():
		form = PostForm()
		if request.method == "POST":
			form = PostForm(request.POST.copy())
			if form.valid():
				poster = request.user
				title = form.cleaned_data["title"]
				content = form.cleaned_data["content"]
				bonus = form.cleaned_data["bonus"]
				post = Ability(abilityNAME=title, abilityDESCRIBE=content,
						logDATE=datetime.datetime.now(),rpREQUIRED=bonus, abilityRAISER=poster)
				post.save()
				return HttpResponseRedirect("/")
		form = PostForm()
		return render_to_response("sells/post.html",{'form': form,})
	return HttpResponseRedirect("/accounts/login/")

def show_ability(request,no):
	'''process show ability page

	judge the kind of request user post and dispatch'''

	if request.user.is_authenticated():
		form = ReplyForm()
		try:
			no=int(no)
			ability=Ability.objects.get(id=no)
			raiser_id = ability.abilityRAISER.id
			if ability.abilityRECEIVER:
				receiver_id = ability.abilityRECEIVER.id
				is_receiver = request.user.id == receiver_id
			else:
				is_receiver = False
			is_raiser = request.user.id == raiser_id
			print is_raiser, is_receiver
		except:
			raise Http404()

		if request.method == 'POST':
			if request.POST.has_key('receive') and request.POST['receive'] == u'领   取':
				receive(request, ability)
			if request.POST.has_key('finish') and request.POST['finish'] == u'结   算':
				finish(request, ability)
				return HttpResponseRedirect("/")
			if request.POST.has_key('reply_tag'):
				save_reply(form, request, ability)
			return HttpResponseRedirect("/sells/%s/" % no)
		else:
			replies = Reply.objects.filter(berepliedABILITY=ability)
		return render_to_response("sells/showability.html", {'request':request, 'ability': ability, 'form': ReplyForm, 'replies': replies, 'is_raiser':is_raiser, 'is_receiver':is_receiver, })
	return HttpResponseRedirect("/accounts/login/")

def show_all_abilities(request):
	abilities = Ability.objects.all()
	return render_to_response("sells/ability.html", {'request': request, 'abilities': abilities,})
	

def receive(request, sell):
	'''Tool method for save ability'''

	ability_raiser = sell.abilityRAISER
	if request.user != ability_raiser:
		if not sell.abilityRECEIVER:
			sell.abilityRECEIVER = request.user
			sell.adoptDATE = datetime.datetime.now()
			sell.save()

def finish(request, sell):
	ability_raiser = sell.abilityRAISER
	raiser_pro = UserProfile.objects.get(user_id = ability_raiser.id)
	raiser_pro.rp += sell.rpREQUIRED
	raiser_pro.save()

def save_reply(form, request, sell):
	'''Tool method for save reply'''

	content = request.POST['content']
	reply = Reply(replyTIME=datetime.datetime.now(), replyUSER=request.user, berepliedABILITY=sell, replyWORDS=content)
	reply.save()
