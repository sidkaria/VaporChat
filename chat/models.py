from django.db import models

class ChatUser(models.Model):
	email = models.EmailField(max_length=200)
	username = models.CharField(max_length=16)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	password = models.CharField(max_length=32)
	GENDER_CHOICES = (
    	('M', 'Male'),
    	('F', 'Female'),
    )
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	confirm_code = models.CharField(max_length=32, default=0)
	confirmed = models.BooleanField(default=0)

	def __str__(self):
		return self.username