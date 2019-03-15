from django.shortcuts import render
from django.http import HttpResponse
from my_web import models
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

per_page = 3

# Create your views here.
def log_index(request):
    if request.session.get('is_login',None):
        customer = models.Customer.objects.get(id=request.session.get('id'))
        if request.method == "POST":
            print(request.POST.get('head'))
            print(request.POST.get('content'))
            obj = models.Log()
            obj.customer = customer
            obj.log_head = request.POST.get('head')
            obj.log_context = request.POST.get('content')
            obj.save()

        objs = models.Log.objects.filter(customer=customer)
        paginator = Paginator(objs,per_page)
        page = request.GET.get('page')
        try:
            objs = paginator.page(page)
        except PageNotAnInteger:
            objs = paginator.page(1)
        except EmptyPage:
            objs = paginator.page(paginator.num_pages)

    return render(request,"log/log_html.html",locals())

def log_detail(request,obj_id):
    obj = models.Log.objects.get(id=obj_id)
    return render(request, "log/log_detail.html", {'obj':obj})