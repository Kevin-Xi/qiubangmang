from django.db import models
#from accounts.model import #
from django.contrib.auth.models import User

#class Task(models.Model):
	#task_type=models.CharField(max_length=1, choices=(('P', 'Publish'), ('R', 'Receive')))
#	poster=models.CharField(max_length=30)
#	receiver=models.CharField(max_length=30, blank=True)
#	title=models.CharField(max_length=60)
#	content=models.TextField(max_length=1000)
#	bonus=models.PositiveIntegerField()

class Mission(models.Model):
	missionNAME = models.CharField(max_length=20)
	missionDESCRIBE = models.TextField(max_length=1000)
	logDATE = models.DateTimeField()
	deadline = models.DateTimeField()
	rpBONUS = models.PositiveIntegerField()
	missionRAISER = models.ForeignKey(User, related_name='User_missionRAISER')
	missionRECEIVER = models.ForeignKey(User, related_name='User_missionRECEIVER', null=True)
	acceptDATE = models.DateTimeField(null=True)


#https://docs.djangoproject.com/en/dev/ref/models/fields/

