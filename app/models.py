from django.db import models

# Create your models here.

class Transaction(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    Amount = models.IntegerField()
    Currency = models.CharField(max_length=3)
    CustomerEmail = models.EmailField(max_length=254)


split_choices = (("FLAT", "FLAT"), ("PERCENTAGE", "PERCENTAGE"), ("RATIO", "RATIO"))

class SplitInfo(models.Model):
    transaction = models.ForeignKey(Transaction, related_name="SplitInfo", on_delete=models.CASCADE)
    SplitType = models.CharField(choices=split_choices, max_length=50)
    SplitValue = models.IntegerField()
    SplitEntityId = models.CharField(max_length=50, primary_key=True, unique=True)

    

class TransactionResponse(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    Balance = models.DecimalField(decimal_places=2, max_digits=8)


class SplitBreakdown(models.Model):
    transaction = models.ForeignKey(TransactionResponse, related_name="SplitBreakdown", on_delete=models.CASCADE)
    SplitEntityId = models.CharField(max_length=50, primary_key=True, unique=True)
    Amount = models.DecimalField(decimal_places=2, max_digits=8)

