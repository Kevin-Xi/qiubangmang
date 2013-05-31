from django.shortcuts import render_to_response
#from posts.models import Post
#from tasks.models import Task
from tasks.models import Mission
from sells.models import Ability

def index(request):
	#posts=Post.objects.all()
	tasks=Mission.objects.all()
	abilities=Ability.objects.all()
	#return render_to_response('index.html',{'request': request,'posts': posts, 'tasks': tasks, 'abilities': abilities, })
	return render_to_response('index.html',
			{'request': request, 'tasks': tasks, 'abilities': abilities, })
