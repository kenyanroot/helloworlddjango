# Generated by Django 3.1 on 2020-09-03 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serverresponse', '0002_auto_20200903_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lmnonline',
            old_name='Ammount',
            new_name='A_mmount',
        ),
        migrations.RenameField(
            model_name='lmnonline',
            old_name='Checkout_request_ID',
            new_name='Checkout_requestID',
        ),
        migrations.RenameField(
            model_name='lmnonline',
            old_name='Merchant_request_ID',
            new_name='Merchant_requestID',
        ),
        migrations.RenameField(
            model_name='lmnonline',
            old_name='Mpesa_receipt_number',
            new_name='Mpesa_receiptnumber',
        ),
        migrations.RenameField(
            model_name='lmnonline',
            old_name='Phone_number',
            new_name='Phonenumber',
        ),
        migrations.RenameField(
            model_name='lmnonline',
            old_name='Result_code',
            new_name='Resultcode',
        ),
        migrations.RenameField(
            model_name='lmnonline',
            old_name='Result_desc',
            new_name='Resultdesc',
        ),
        migrations.RenameField(
            model_name='lmnonline',
            old_name='Transaction_date',
            new_name='Transactiondate',
        ),
    ]
