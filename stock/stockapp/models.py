from django.db import models


# Create your models here.

class Stock(models.Model):
	date = models.DateField()
	stock_id = models.CharField(max_length=20)
	Open = models.IntegerField()
	High = models.IntegerField()
	Low = models.IntegerField()
	Close = models.IntegerField()
	AdjClose = models.FloatField()
	Volume = models.IntegerField()

	def __str__(self):
		return f'{self.date} - {self.stock_id} - Open => {self.Open}, Close => {self.Close}, High => {self.High}'
