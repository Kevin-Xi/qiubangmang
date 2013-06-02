from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from forms import RegisterForm, LoginForm
from django.template import RequestContext
from tasks.models import Mission
from sells.models import Ability
from accounts.models import UserProfile

def register(request):
    template_var = {}
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            sex = form.cleaned_data["sex"]
            phone = form.cleaned_data["phone"]
            qq = form.cleaned_data["qq"]
            describe = form.cleaned_data["describe"]
            user = User.objects.create_user(username, email, password)
            user.save()
            user_pro = UserProfile(user = user, 
            	sex = sex, phone = phone, qq = qq, describe = describe,
            	acceptNUMBER = 0, raiseNUMBER = 0, userLEVEL = 0, rp = 0)
            user_pro.save()
            _login(request, username, password)
            return HttpResponseRedirect("/accounts/welcome")
    template_var["form"] = form
    return render_to_response("accounts/register.html", template_var, context_instance = RequestContext(request))

def login(request):
	template_var={}
	form=LoginForm()
	if request.method=="POST":
		form=LoginForm(request.POST.copy())
		if form.is_valid():
			_login(request,form.cleaned_data['username'],form.cleaned_data['password'])
			return HttpResponseRedirect("/accounts/welcome/")
			#return HttpResponseRedirect(url)
	template_var['form']=form
	return render_to_response("accounts/login.html",template_var,context_instance=RequestContext(request))

def welcome(request):
	if request.user.is_authenticated():
		username=request.user.username
		url=request.get_full_path()
		return render_to_response('accounts/welcome.html', {'username': username, 'url': url, })
	else:
		return HttpResponseRedirect("/accounts/login/")

def _login(request, username, password):
	ret=False
	user=authenticate(username=username, password=password)
	if user:
		if user.is_active:
			auth_login(request, user)
			ret=True
		else:
			print '1'
	else:
		print '2'
	return ret

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect("/")

def homepage(request, user_id):
	if request.user.is_authenticated():
		try:
			user=User.objects.get(id=user_id)
		except:
			raise Http404()
		received_tasks = Mission.objects.filter(missionRAISER=user).exclude(missionRECEIVER=None)
		unreceived_tasks = Mission.objects.filter(missionRAISER=user, missionRECEIVER=None)
		received_abilities=Ability.objects.filter(abilityRAISER=user).exclude(abilityRECEIVER=None)
		unreceived_abilities=Ability.objects.filter(abilityRAISER=user, abilityRECEIVER=None)
		return render_to_response("accounts/homepage.html", {'request': request, 'user': user, 'received_tasks': received_tasks, 'unreceived_tasks': unreceived_tasks, 'received_abilities': received_abilities, 'unreceived_abilities': unreceived_abilities, })
	return HttpResponseRedirect("/accounts/login/")

def info(request):
	if request.user.is_authenticated():
		try:
			user = User.objects.get(id = request.user.id)
			user_pro = UserProfile.objects.get(user_id = user.id)
			form = RegisterForm()
			email_judge = False
			username_judge = False
			if request.method == 'POST':
				form = RegisterForm(request.POST.copy())
				if form.is_valid():
					email = form.cleaned_data["email"]
					username = form.cleaned_data["username"]
					password = form.cleaned_data["password"]
					sex = form.cleaned_data["sex"]
					phone = form.cleaned_data["phone"]
					qq = form.cleaned_data["qq"]
					describe = form.cleaned_data["describe"]
					#for judege
					try:
						tmp = User.objects.get(email = email)
						if tmp.id != user.id: email_judge = True
						else: email_judge = False
					except:	
						email_judge = False
					try:
						tmp = User.objects.get(username = username)
						if tmp.id != user.id: username_judge = True
						else: username_judge = False
					except:	
						username_judge = False
					if email_judge or username_judge:
						return render_to_response("accounts/info.html", {'email_judge':email_judge, 'username_judge':username_judge, }) 
					else:
						user.email = email
						user.username = username
						user.set_password(password)
						user_pro.sex = sex
						user_pro.phone = phone
						user_pro.qq = qq
						user_pro.describe = describe
						user.save()
						user_pro.save()
						return HttpResponseRedirect("/")
			return render_to_response("accounts/info.html", {'email_judge':email_judge, 'username_judge':username_judge, })
		except:
			raise Http404()
	return HttpResponseRedirect("/accounts/login/")
