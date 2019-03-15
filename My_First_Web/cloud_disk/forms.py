from django import forms
from my_web import models

class Cloud_DickForm(forms.ModelForm):
    def __new__(cls, *args, **kwargs):
        for field_name,field_obj in cls.base_fields.items():
            # 'if field_name == "customer":
            field_obj.widget.attrs["color"] = "black"
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Cloud_Disk
        fields = ['file']
