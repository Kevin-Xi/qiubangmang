'''Process the index request'''
from django.shortcuts import render_to_response
from tasks.models import Mission
from sells.models import Ability

def index(request):
	tasks = Mission.objects.all()
	abilities = Ability.objects.all()
	return render_to_response('index.html',
			{'request': request, 'tasks': tasks, 'abilities': abilities, })
