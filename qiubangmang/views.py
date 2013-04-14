from django.shortcuts import render_to_response
from posts.models import Post
from tasks.models import Task

def index(request):
	posts=Post.objects.all()
	tasks=Task.objects.all()
	return render_to_response('index.html',{'request': request,'posts': posts, 'tasks': tasks, })
	#return render_to_response('index.html',)
