from django.contrib import admin

# Register your models here.
from  serverresponse.models import LMNOnline

admin.site.register(LMNOnline)

class LMNOnlineAdmin(admin.ModelAdmin):
    list_display = ('Phonenumber','A_mmount','Transactiondate','Resultdesc')