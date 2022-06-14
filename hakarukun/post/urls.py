from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('append/<id>/<value>', views.post, name='post'),
]