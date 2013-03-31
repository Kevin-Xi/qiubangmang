from django.db import models

class Post(models.Model):
	title=models.CharField(max_length=60)
	poster=models.IntegerField()
	content=models.TextField()
