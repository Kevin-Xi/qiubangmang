#-- coding:utf-8 --
'''Process all request relatived to tasks

include post and show page'''

import datetime
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from models import Mission
from forms import PostForm
from reply.forms import ReplyForm
from reply.models import Reply
from accounts.models import UserProfile

def post(request):
	'''process post page

	judge user's authenticate status and save valid post, store raiseNUMBER of user'''

	if request.user.is_authenticated():
		form = PostForm()
		if request.method == "POST":
			form = PostForm(request.POST.copy())
			if form.valid():
				poster = request.user
				title = form.cleaned_data["title"]
				content = form.cleaned_data["content"]
				bonus = form.cleaned_data["bonus"]
				deadline = form.cleaned_data["deadline"]
				post = Mission(missionNAME=title, missionDESCRIBE=content,
						logDATE=datetime.datetime.now(), deadline=deadline,
						rpBONUS=bonus, missionRAISER=poster, closed=False)
				post.save()

				poster_pro = UserProfile.objects.get(user_id=request.user.id) 
				poster_pro.raiseNUMBER += 1
				poster_pro.save()
				return HttpResponseRedirect("/")
		form = PostForm()
		return render_to_response("tasks/post.html",{'form': form,})
	return HttpResponseRedirect("/accounts/login/")

def show_task(request,no):
	'''process show task page

	judge the kind of request user post and dispatch'''

	if request.user.is_authenticated():
		form = ReplyForm()
		try:
			no = int(no)
			task = Mission.objects.get(id=no)
			if task.closed:
				return HttpResponseRedirect("/accounts/%s/" % request.user.id)
			raiser_id = task.missionRAISER.id
			if task.missionRECEIVER:
				receiver_id = task.missionRECEIVER.id
				is_receiver = request.user.id == receiver_id
			else:
				is_receiver = False
			is_raiser = request.user.id == raiser_id
		except:
			raise Http404()

		if request.method == 'POST':
			if request.POST.has_key('receive') and request.POST['receive'] == '领取！':
				receive(request, task)
			if request.POST.has_key('finish') and request.POST['finish'] == '结算！':
				finish(request, task)
			if request.POST.has_key('reply_tag'):
				save_reply(form, request, task)
			return HttpResponseRedirect("/tasks/%s/" % no)
		else:
			replies = Reply.objects.filter(berepliedMISSION=task)
			return render_to_response("tasks/showtask.html", {'task': task, 'form': ReplyForm, 'replies': replies, 'is_raiser':is_raiser, 'is_receiver':is_receiver,})
	return HttpResponseRedirect("/accounts/login/")

def receive(request, task):
	'''Tool method for save task'''

	task_raiser = task.missionRAISER
	if request.user != task_raiser:
		if not task.missionRECEIVER:
			task.missionRECEIVER = request.user
			task.acceptDATE = datetime.datetime.now()
			task.save()

def save_reply(form, request, task):
	'''Tool method for save reply'''

	content = request.POST['content']
	reply = Reply(replyTIME=datetime.datetime.now(), replyUSER=request.user, berepliedMISSION=task, replyWORDS=content)
	reply.save()

def finish(request, task):

	task.closed = True;
	task.save()
	receiver_pro = UserProfile.objects.get(user_id = task.missionRECEIVER.id)
	receiver_pro.rp += task.rpBONUS;
	receiver_pro.userLEVEL = 1+receiver_pro.rp/100
	receiver_pro.save()
