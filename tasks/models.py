from django.db import models

class Task(models.Model):
	#task_type=models.CharField(max_length=1, choices=(('P', 'Publish'), ('R', 'Receive')))
	poster=models.CharField(max_length=30)
	receiver=models.CharField(max_length=30, blank=True)
	title=models.CharField(max_length=60)
	content=models.TextField(max_length=1000)
	bonus=models.PositiveIntegerField()

	def add(username):
		receiver=username
