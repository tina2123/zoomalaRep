from django.db import models

# Create your models here.
class Destination(models.Model):
	res= models.CharField(max_length=100, default='User name')
	title= models.CharField(max_length=200, default='Post title')
	desc= models.TextField(default='description')
	img= models.ImageField(upload_to='pics', default='img/logo.png')
	timestamp= models.DateTimeField(auto_now=False, auto_now_add=True)

	 
	