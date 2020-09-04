from django.contrib import admin

# Register your models here.
from  greetings.models import Namecomment
admin.site.register(Namecomment)


class Namecomment(admin.ModelAdmin):
    list_display = ('name','comment','phone_number')