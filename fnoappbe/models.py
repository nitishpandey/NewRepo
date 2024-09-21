from django.db import models
import os
from django.conf import settings
# Create your models here.
#short term positions table
from django.db import models

 
class Position(models.Model):
    exchange = models.CharField(null =True, blank= True, max_length=10)
    value = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)  # Adjust precision as needed
    pnl = models.DecimalField(null =True, blank= True,  max_digits=10, decimal_places=2)
    product = models.CharField(null =True, blank= True, max_length=10)
    instrument_token = models.CharField(null =True, blank= True, max_length=20)  # Adjust length if needed
    average_price = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    buy_value = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    overnight_quantity = models.IntegerField(null =True, blank= True, )
    day_buy_value = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    day_buy_price = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    overnight_buy_amount = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    overnight_buy_quantity = models.IntegerField(null =True, blank= True, )
    day_buy_quantity = models.IntegerField(null =True, blank= True, )
    day_sell_value = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    day_sell_price = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    day_sell_quantity = models.IntegerField(null =True, blank= True, )
    quantity = models.IntegerField(null =True, blank= True, )
    last_price = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    unrealised = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    realised = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    sell_value = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    tradingsymbol = models.CharField(null =True, blank= True, max_length=20)  # Adjust length if needed
    close_price = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    buy_price = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(null =True, blank= True, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tradingsymbol