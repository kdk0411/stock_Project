from django.db import models


# Create your models here.

class Stock(models.Model):
	date = models.DateField()
	stock_id = models.CharField(max_length=20)
	Open = models.FloatField()
	High = models.FloatField()
	Low = models.FloatField()
	Close = models.FloatField()
	AdjClose = models.FloatField()
	Volume = models.FloatField()

	def __str__(self):
		return f'{self.date} - {self.stock_id} - Open => {self.Open}, Close => {self.Close}, High => {self.High}'


"""
	005930.KS : Samsung Electronics
	000660.KS : SK hynix
	373220.KS : LG Energy Solution
	035420.KS : NAVER
	005380.KS : Hyundai Motor
	000270.KS : Kia
	035720.KS : Kakao
	AAPL : Apple
	TSLA : Tesla	
"""