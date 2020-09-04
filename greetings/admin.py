from django.contrib import admin

# Register your models here.
from  greetings.models import Namecomment


class NamecommentAdmin(admin.ModelAdmin):
    list_display = ('name','comment','phone_number')

admin.site.register(Namecomment,NamecommentAdmin)
