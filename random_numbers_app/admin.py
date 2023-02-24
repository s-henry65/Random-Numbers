from django.contrib import admin
from . import models

class GameAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    
admin.site.register(models.LotteryResults, GameAdmin)
