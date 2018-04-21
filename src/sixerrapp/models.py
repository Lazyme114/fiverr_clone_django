from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.CharField(max_length=500)
	about = models.TextField()
	slogan = models.CharField(max_length=250)

	def __str__(self):
		return self.user.username

class Gig(models.Model):
	CATEGORY_CHOICES = (
		("GD", "Graphics & Design"),
		("DM", "Digital Marketing"),
		("VA", "Video & Animation"),
		("MA", "Music & Audio"),
		("PT", "Programming & Tech"),
	)

	title = models.CharField(max_length=250)
	category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	photo = models.FileField(upload_to='gigs')
	status = models.BooleanField(default=True)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Pruchase(models.Model):
	gig = models.ForeignKey(Gig)
	buyer = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.gig.title

class Review(models.Model):
	gig = models.ForeignKey(Gig)
	user = models.ForeignKey(User)
	content = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content