from django.contrib import admin
from Chat.models import Asker,BotAi,Botbody,Askerbody
# Register your models here.
admin.site.register(Asker)
class Asker(admin.ModelAdmin):
    list_display = ['name', 'body']

admin.site.register(BotAi)

class BotAi(admin.ModelAdmin):
    list_display = ['name', 'BotAns']

admin.site.register(Askerbody)
admin.site.register(Botbody)
