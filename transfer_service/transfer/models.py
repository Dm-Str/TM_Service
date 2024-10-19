from django.db import models


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=50, unique=True)
    from_account = models.CharField(max_length=20)
    to_account = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    starus = models.CharField(max_length=20) # PENDING, COMPLETED, FAILED
    timestamp = models.DateTimeField(auto_now_add=True)
