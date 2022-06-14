from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'main'

urlpatterns = [
    path('home', views.home, name='home'),
    #path('intake', views.intake, name='intake'),
    path('setting', views.setting, name='setting'),
    path('intake/', views.GreetView.as_view(), name='intake'),
    path('my_module', views.My_module.as_view(), name='my_module'),
    path('add_module', views.Add_module.as_view(), name='add_module'),
    path('edit_module/<id>', views.Edit_module.as_view(), name='edit_module'),
    path('del_module/<id>', views.Del_module.as_view(), name='del_module'),
]