from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	#email=models.EmailField(max_length=30)
	#username=models.CharField(max_length=30)
	#password=models.CharField(max_length=10)
	user=models.OneToOneField(User)

	sex=models.CharField(max_length=2)
	phone=models.CharField(max_length=15)
	qq=models.CharField(max_length=12)
	describe=models.CharField(max_length=100)
