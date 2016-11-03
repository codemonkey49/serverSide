from django.contrib import admin
from models import watchedData,itemData,transactionData,stockData,commandsDB
# Register your models here.

class commandsAdmin(admin.ModelAdmin):
    list_display=("PID","bs","itemID","amt","price")
    list_filter = ['PID']
class stockAdmin(admin.ModelAdmin):
    list_display=("PID","itemID","amt","price")
    list_filter = ['PID']
class transactionAdmin(admin.ModelAdmin):
    list_display=("PID","bs","itemID","amt","price","currentLiquid")
    list_filter = ['PID']
class itemInfoAdmin(admin.ModelAdmin):
    list_display=("itemID","price","date")
    list_filter = ['itemID']
class watchedAdmin(admin.ModelAdmin):
    list_display=("userWatched","machineWatched","itemID")
    list_filter = ['userWatched',"machineWatched"]
admin.site.register(watchedData,watchedAdmin)
admin.site.register(itemData,itemInfoAdmin)
admin.site.register(transactionData,transactionAdmin)
admin.site.register(stockData,stockAdmin)
admin.site.register(commandsDB,commandsAdmin)
