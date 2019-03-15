from django.shortcuts import render
from django.http import HttpResponse
from my_wechat.task import get_wechat_data

# Create your views here.

def wechat_index(request):

    try:
        str = 'city'
        # friends = get_wechat_data.get_friend()
        city,city_count = get_wechat_data.get_friend(str)
        str = 'province'
        province,province_count = get_wechat_data.get_friend(str)
        str = 'sex'
        sex = get_wechat_data.get_friend(str)
        for k,v in sex.items():
            if k == 1:
                male = v
            elif k == 2:
                female = v
            else:
                el = v
    except Exception as e:
        ele = """<img >"""
        return HttpResponse("")
    return render(request,"my_wechat/wechat.html",locals())