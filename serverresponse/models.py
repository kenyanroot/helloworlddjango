from django.db import models

# Create your models here.
class  LMNOnline(models.Model):
    Merchant_requestID=models.CharField(max_length=50)
    #Checkout_requestID=models.CharField(max_length=40)
    Resultcode=models.IntegerField()
    Resultdesc =models.CharField(max_length=120)
    A_mmount     =models.FloatField()
    Mpesa_receiptnumber=models.CharField(max_length=20)
    Transactiondate =models.DateTimeField()
    Phonenumber =models.CharField(max_length=13)
    def __str__(self):
        return f"{self.Phonenumber} has sent  {self.A_mmount} at {self.Transactiondate}"
