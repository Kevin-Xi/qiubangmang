#-- coding:utf-8 --
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from models import Post
from forms import PostForm

def post(request):
	# form, auth, database, show
	if request.user.is_authenticated():
		form=PostForm()
		if request.method=="POST":
			form=PostForm(request.POST.copy())
			if form.is_valid():
				title=form.cleaned_data["title"]
				poster=request.user.username
				content=form.cleaned_data["content"]
				post=Post(title=title,poster=poster,content=content)
				post.save()
				return HttpResponseRedirect("/")
		form=PostForm()
		return render_to_response("posts/post.html",{'form':form,})
	return HttpResponseRedirect("/accounts/login/")

def showpost(request,no):
	try:
		no=int(no)
	except ValueError:
		raise Http404()
	post=Post.objects.filter(id=no).values()[0]
	print post
	title=post['title']
	poster=post['poster']
	content=post['content']
	return render_to_response("posts/showpost.html",{'title':title,'poster':poster,'content':content,})
