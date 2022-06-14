#from hakarukun.accounts import models
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import mymodule, names
from django.template import loader
import json
import datetime
from django.utils.timezone import make_aware
from django.utils import timezone
from django.http.response import JsonResponse
import pytz
# Create your views here.
def home(request):
    #print(request.user)
    st,names=get_intake(1440,request.user)
    data=zip(names,st)
    context = {
        'data':data,
        'sum':sum(st)
        }
    #print(get_intake(1440,request.user))
    return render(request, 'toppage.html',context)
def get_intake(delta,username):
        """jQuery に対してレスポンスを返すメソッド"""
        #data=names(uuid=form.cleaned_data.get('name'))
        
        #data.save()
        val=list()
        names=list()
        user_module=mymodule.objects.values('uuid').filter(username=username)
        module_nemes=mymodule.objects.values('screenname').filter(username=username)

                
        st=list()
        
        for id in user_module:#モジュールごとの値を取得
            st.append(0)
            now=0
            count=0
            for i in weightdata.objects.values('content','pub_date').filter(uuid=id["uuid"]).order_by('-pub_date')[:1440]:
                #print(i["content"],i["pub_date"])
                if now==0:
                    now=int(i["content"])
                else:
                    
                    if now-int(i["content"])<0:
                        st[-1]-=now-int(i["content"])
                    now=int(i["content"])
                #val[-1].append(i["content"])
                
        
    
        for i in module_nemes:
            #print(i["screenname"])
            names.append(i["screenname"])

        return st,names


@login_required
def setting(request):
    return render(request,'setting.html')





from django.views.generic import FormView

from . import forms
from main.models import mymodule
from post.models import weightdata
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class GreetView(FormView):
    template_name = 'intake.html'  # テンプレート名(htmlファイル名)
    form_class = forms.GreetForm
    success_url = 'main/intake'
    #<!-- 10min,30min,1h,2,6,12,24 -->
    
    def get(self, request, *args, **kwargs):
        
        st,names=get_intake(1440,request.user)
        data=zip(names,st)

        time ,val,nemes=self.ajax_response(3,request.user)
        data=zip(nemes,val)
        return render(request, 'intake.html', {"time":time,"data":data,"length":len(nemes),"sum":sum(st)})


    def post(self, request, *args, **kwargs):
        
        #delta=delta_list[int(request.POST["sliderval"])]
        if request.is_ajax():
            """Ajax 処理を別メソッドに切り離す"""
            #print('### Ajax request')
            # time ,val,nemes=self.ajax_response(1028,60,request.user)
            # return JsonResponse(data={"time":time,"val":val[0],"nemes":names})  
            st,names=get_intake(1440,request.user)
            time ,val,names=self.ajax_response(int(request.POST["sliderval"]),request.user)
            return JsonResponse(data= {"time":time,"val":val,"names":names,"len":3,"sum":sum(st)})     
        # Ajax 以外のPOSTメソッドの処理
        #return self.ajax_response(1028,delta,request.user)

    def ajax_response(self,delta,username):
        """jQuery に対してレスポンスを返すメソッド"""
        #data=names(uuid=form.cleaned_data.get('name'))
        #data.save()
        delta_list=[10,30,60,120,360,720,1440]
    
        skip_list=[1,1,1,3,3,6,12]
        val=list()
        time=list()
        times=list()
        names=list()
        user_module=mymodule.objects.values('uuid').filter(username=username)
        module_nemes=mymodule.objects.values('screenname').filter(username=username)
        for i in range(0,delta_list[delta],skip_list[delta]):#時間ごとで検索をかけるためにdeltaおきの時刻を取得
            now=timezone.datetime.strptime(timezone.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M")
            st=now+ timezone.timedelta(minutes=-1*i)
            
            times.append(st)
            #print(st.minute)
            if st.minute <=9:
                time.append(str((st.hour+9)%24)+":0"+str(st.minute))
            else:
                time.append(str((st.hour+9)%24)+":"+str(st.minute))

        time.reverse()    
        times.reverse() 
        lastval=0
        for id in user_module:#モジュールごとの値を取得
            val.append(list())
            for i in times:
                #print(i)
                try:
                    weightdata.objects.values('pub_date','content').filter(uuid=id["uuid"],pub_date=i)[0]["content"]
                    lastval=weightdata.objects.values('pub_date','content').filter(uuid=id["uuid"],pub_date=i)[0]["content"]
                    val[-1].append(lastval)
                    
                except:
                    val[-1].append(lastval)
                    #val[-1].append("null")


        for i in module_nemes:
            #print(i["screenname"])
            names.append(i["screenname"])

        return time ,val,names
        # print(prm)
        #print(type(prm))
        # print("pass")
        #return prm

class My_module(FormView):
    
    def get(self, request, *args, **kwargs):
        template = loader.get_template('toppage.html')
        st=mymodule.objects.filter(username= request.user)
        #print(st)
        data=list()
        for i in st:
            #uuid.append(i.uuid)
            #password.append(i.modulepassword)
            data.append([i.uuid,i.screenname,i.modulepassword])
        context = {
        'data': data
        }
        return render(request, 'my_module.html', context)
        #return render(request,'toppage.html')

    


class Add_module(FormView):
    form_class = forms.Add_module
    template_name = 'add_module.html'
    @login_required
    def get_success_url(self):
        
        return render(form_class, 'add_module.html')
    
    def post(self, request, *args, **kwargs):
        print("addmodule post")
        print(request.user)
        print(request.POST['uuid'])
        print(request.POST['modulepassword'])
        st=mymodule.objects.filter(uuid= request.POST['uuid'],username=request.user)#自分が所有している
        st1=mymodule.objects.filter(uuid= request.POST['uuid'])#すでに取得されている
        print(len(st))
        if len(st)==0 and len(st1)==0:#自分が登録していなくてまだuuidが使用されていない場合
            data=mymodule(username =request.user ,uuid=request.POST['uuid'],screenname=request.POST['screenname'],modulepassword=request.POST['modulepassword'])
            data.save()
            context = {
            'massage': request.POST['screenname']+"は、正常に追加されました",
            }
        
        elif len(st)!=0:#自分が所有している
            context = {
            'massage': request.POST['screenname']+"のuuidは、すでにあなたが追加しています",
            }
        elif len(st1)!=0:#すでに取得されている
            context = {
            'massage': request.POST['screenname']+"のuuidは、すでに使用されています。",
            }
        


        return render(request, 'toppage.html',context)

class Edit_module(FormView):
    form_class = forms.Edit_module
    template_name = 'my_module_edit.html'
    
    
    def get_success_url(self):
        print("get")
        return render(form_class, 'my_module_edit.html')
    
    def post(self, request,id, *args, **kwargs):

        st=mymodule.objects.filter(uuid= id,username=request.user)[0]
        st.screenname=request.POST['screenname']
        st.modulepassword=request.POST['modulepassword']
        st.save()
        print(st)
        context = {
            'massage': id,
            }
        return render(request, 'toppage.html',context)
    
class Del_module(FormView):

    
    def get(self, request,id, *args, **kwargs):
        print("get")
        context = {
            'uuid': id,
            }
        return render(request,'my_module_del.html',context)

    def post(self, request,id, *args, **kwargs):
        print("post")
        print(request.user)
        print(id)
        name=mymodule.objects.filter(uuid= id,username=request.user)[0]
        st=mymodule.objects.filter(uuid= id,username=request.user).delete()
        context = {
            'massage': name.screenname +"を削除しました",
            }
        return render(request, 'toppage.html',context)



