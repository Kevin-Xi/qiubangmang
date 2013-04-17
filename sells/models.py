from django.db import models

class Ability(models.Model):
	poster=models.CharField(max_length=30)
	receiver=models.CharField(max_length=30, blank=True)
	title=models.CharField(max_length=60)
	content=models.TextField(max_length=1000)
	bonus=models.PositiveIntegerField()
