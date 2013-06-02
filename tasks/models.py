from django.db import models
from django.contrib.auth.models import User

class Mission(models.Model):
	'''Mission model

	follow database design doc'''

	missionNAME = models.CharField(max_length=80)
	missionDESCRIBE = models.TextField(max_length=1000)
	logDATE = models.DateTimeField()
	deadline = models.DateTimeField()
	rpBONUS = models.PositiveIntegerField()
	missionRAISER = models.ForeignKey(User, related_name='User_missionRAISER')
	missionRECEIVER = models.ForeignKey(User, related_name='User_missionRECEIVER', null=True)
	acceptDATE = models.DateTimeField(null=True)
	closed = models.BooleanField()
