from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Asker(models.Model):
    Date = models.DateField(default=date.today)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return str(self.user)
    
class Askerbody(models.Model):
    Date = models.DateField(default=date.today)
    asker = models.ForeignKey(Asker,on_delete=models.CASCADE)
    body = models.TextField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return str(self.asker.user)



class BotAi(models.Model):
    Date = models.DateField(default=date.today)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
   

    def __str__(self):
        return str(self.user)
    
class Botbody(models.Model):
    Date = models.DateField(default=date.today)
    bot = models.ForeignKey(BotAi,on_delete=models.CASCADE)
    BotAns= models.TextField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return str(self.bot.user)
