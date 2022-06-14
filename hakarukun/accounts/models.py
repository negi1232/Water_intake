from django.db import models
from django.contrib.auth.models import User



class user_data(models.Model):
    #pub_date = models.DateTimeField(default=timezone.datetime.strptime(timezone.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M"))#追加日時
    username = models.CharField(max_length=200)#追加日時
    linetoken= models.CharField(max_length=200)
    temperature=models.CharField(max_length=200)
    weight=models.CharField(max_length=200)

