from django.db import models

# Create your models here.
class names(models.Model):
    
    uuid = models.CharField(max_length=200)#追加時のモジュールナンバー

class mymodule(models.Model):
    #pub_date = models.DateTimeField(default=timezone.datetime.strptime(timezone.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M"))#追加日時
    username = models.CharField(max_length=200)#追加日時
    screenname = models.CharField(max_length=200)#追加日時
    uuid = models.CharField(max_length=200)#追加時のモジュールナンバー
    modulepassword=models.CharField(max_length=200)