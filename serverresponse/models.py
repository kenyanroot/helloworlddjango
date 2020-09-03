from django.db import models

# Create your models here.
class  LMNOnline(models.Model):
    Merchant_request_ID=models.CharField(max_length=50)
    Checkout_request_ID=models.CharField(max_length=20)
    Result_code=models.IntegerField()
    Result_desc =models.CharField(max_length=120)
    Ammount     =models.FloatField()
    Mpesa_receipt_number=models.CharField(max_length=20)
    Transaction_date =models.DateTimeField()
    Phone_number =models.CharField(max_length=13)
