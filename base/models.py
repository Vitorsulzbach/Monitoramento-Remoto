from django.db import models

class amostra(models.Model):
	date = models.DateTimeField(auto_now_add=False)
	x0 = models.CharField(max_length=20)
	x1 = models.CharField(max_length=20)
	x2 = models.CharField(max_length=20)
	x3 = models.CharField(max_length=20)
	x4 = models.CharField(max_length=20)
	x5 = models.CharField(max_length=20)
	x6 = models.CharField(max_length=20)
	x7 = models.CharField(max_length=20)
	x8 = models.CharField(max_length=20)
	x9 = models.CharField(max_length=20)
	x10 = models.CharField(max_length=20)
	x11 = models.CharField(max_length=20)
	x12 = models.CharField(max_length=20)
	x13 = models.CharField(max_length=20)
	x14 = models.CharField(max_length=20)
	x15 = models.CharField(max_length=20)
	x16 = models.CharField(max_length=20)
	x17 = models.CharField(max_length=20)
	x18 = models.CharField(max_length=20)
	x19 = models.CharField(max_length=20)
	x20 = models.CharField(max_length=20)
	x21 = models.CharField(max_length=20)
	x22 = models.CharField(max_length=20)
	x23 = models.CharField(max_length=20)
	x24 = models.CharField(max_length=20)
	média = models.CharField(max_length=20)
	sigma = models.CharField(max_length=20)
	def __str__(self):
		return self.média

class Graphic(models.Model):
	date_added = models.DateTimeField(auto_now_add=True)
	year = models.CharField(max_length=4)
	month = models.CharField(max_length=2)
	day = models.CharField(max_length=2)
	hour = models.CharField(max_length=2)
	minu = models.CharField(max_length=2)
	year1 = models.CharField(max_length=4)
	month1 = models.CharField(max_length=2)
	day1 = models.CharField(max_length=2)
	hour1 = models.CharField(max_length=2)
	minu1 = models.CharField(max_length=2)
	img = models.ImageField(upload_to='graphs', blank=True)
	def __str__(self):
		return str(self.date_added)
