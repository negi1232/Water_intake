


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class weightdata(models.Model):
    #pub_date = models.DateTimeField(default=timezone.datetime.strptime(timezone.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M"))#追加日時
    pub_date = models.CharField(max_length=200)#追加日時
    uuid = models.CharField(max_length=200)#追加時のモジュールナンバー
    content = models.TextField()#データ

#timezone.datetime.strptime(timezone.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M")