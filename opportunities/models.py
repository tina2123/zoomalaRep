from django.db import models
from datetime import date

# Create your models here.
class Post(models.Model):
	company= models.CharField(max_length=100, default=' ')
	title= models.CharField(max_length=200, default=' ')
	desc= models.TextField(default=' ')
	img= models.ImageField(upload_to='pics', default='img/logo.png')
	deadline=models.DateField(default=date.today())
	timestamp= models.DateTimeField(auto_now=False, auto_now_add=True)
	

	 
	