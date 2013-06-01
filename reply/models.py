from django.db import models
from django.contrib.auth.models import User
from tasks.models import Mission
from sells.models import Ability

class Reply(models.Model):
	replyTIME = models.DateTimeField()
	replyUSER = models.ForeignKey(User, related_name='User_reply')
	berepliedREPLY = models.ForeignKey('self', related_name='Reply_bereplied', null=True)
	berepliedMISSION = models.ForeignKey(Mission, related_name='Mission_bereplied', null=True)
	berepliedABILITY = models.ForeignKey(Ability, related_name='Ability_bereplied', null=True)
	replyWORDS = models.TextField(max_length=400)
