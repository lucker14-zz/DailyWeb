from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 140)
	body = models.TextField()
	date = models.DateField()
	video = models.FileField()

	def __str__(self):
		return self.title
