from django.db import models

# Create your models here.

# For JSON Model
class StockMarketData(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=50)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

# For SQL Model
class SQLSMData(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=50)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    