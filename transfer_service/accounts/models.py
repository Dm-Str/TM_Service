from django.db import models


class Account(models.Model):
    account_id = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    сurrency = models.CharField(max_length=3)
    timestamp = models.DateTimeField(auto_now_add=True)
