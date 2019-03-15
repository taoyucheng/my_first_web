from django import forms
from my_web import models
from captcha.fields import CaptchaField

class CustomerForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(CustomerForm,self).__init__(*args,**kwargs)
        self.fields['phone'].label = '电话号码'
        self.fields['password'].label = '密码'

    def __new__(cls, *args, **kwargs):
        for field_name,field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'
            field_obj.widget.attrs['color'] = 'white'
            if field_name == "birthday":
                field_obj.widget.attrs['type'] = 'date'

        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Customer
        fields = '__all__'

class CustomerChangeForm(forms.ModelForm):

    def __new__(cls, *args, **kwargs):
        for field_name,field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'
            field_obj.widget.attrs['color'] = 'white'
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Customer
        fields = '__all__'
        exclude = ['phone','password']



class Userform(forms.Form):
    phone = forms.CharField(label="电话号码",max_length=128)
    password = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput)
