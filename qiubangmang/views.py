from django.shortcuts import render_to_response
from posts.models import Post

def index(request):
	posts=Post.objects.all()
	return render_to_response('index.html',{'request': request,'posts': posts})
	#return render_to_response('index.html',)
