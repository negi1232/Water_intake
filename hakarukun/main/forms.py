from django import forms
from .models import mymodule

class GreetForm(forms.Form):
    name = forms.CharField(label='あなたの名前は？')
    
class Add_module(forms.ModelForm):
    """ユーザー情報更新フォーム"""

    class Meta:
        model = mymodule
        fields = ('uuid','screenname','modulepassword')

class Edit_module(forms.ModelForm):
    """ユーザー情報更新フォーム"""

    class Meta:
        model = mymodule
        fields = ('screenname','modulepassword')

class Add_module(forms.ModelForm):
    """ユーザー情報更新フォーム"""

    class Meta:
        model = mymodule
        fields = ('uuid','screenname','modulepassword')