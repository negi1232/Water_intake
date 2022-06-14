from django.shortcuts import render
from django.http import HttpResponse
from post.models import weightdata
# Create your views here.
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.utils import dateformat
@method_decorator(csrf_exempt)
def post(request,id,value):
    #print("post")
    #print(id)
    #同じ時間にポストされたものがあれば追加しない
    st=weightdata.objects.filter(uuid=id , pub_date=timezone.datetime.strptime(timezone.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M"))
    #print(len(st))
    if len(st)==0:
        data=weightdata(pub_date=timezone.datetime.strptime(timezone.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M") ,uuid=id,content=value)
        data.save()
    return render(request, 'post.html')

