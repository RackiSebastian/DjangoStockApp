from django.db import models

#Database shtuff 
#Two step process 
#Create and then migrate. 
######2 Steps vvv#######
#python mange.py createmigrations
#python manage.py migrate 
class Stock(models.Model):
	ticker = models.CharField(max_length= 100)

	def __str__(self):
		return self.ticker #Admin area debugging and things



