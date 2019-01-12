from django.contrib import admin
from .models import GBP_m15

# Register your models here.

class FarmAdmin(admin.ModelAdmin):
	list_display = ("timeStamp","date", "time", "open", "high","low", "close","chinaTime")

admin.site.register(GBP_m15, FarmAdmin)