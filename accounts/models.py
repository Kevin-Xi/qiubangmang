from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	
	user=models.OneToOneField(User)

	sex=models.CharField(max_length=2, null = True)
	phone=models.CharField(max_length=15)
	qq=models.CharField(max_length=12, null = True)
	describe=models.CharField(max_length=100, null = True)
	acceptNUMBER=models.IntegerField()
	raiseNUMBER=models.IntegerField()
	userLEVEL=models.IntegerField()
	rp=models.IntegerField()
