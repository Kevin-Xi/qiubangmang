from django.db import models
from django.contrib.auth.models import User

class Ability(models.Model):
	'''Ability model

	follow database design doc'''

	abilityNAME = models.CharField(max_length=80)
	abilityDESCRIBE = models.TextField(max_length=1000)
	logDATE = models.DateTimeField()
	rpREQUIRED = models.PositiveIntegerField()
	abilityRAISER = models.ForeignKey(User, related_name='User_abilityRAISER')
	abilityRECEIVER = models.ForeignKey(User, related_name='User_abilityRECEIVER', null=True)
	adoptDATE = models.DateTimeField(null=True)
