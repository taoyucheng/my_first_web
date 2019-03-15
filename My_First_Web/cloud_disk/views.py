from django.shortcuts import render,redirect
from django.http import HttpResponse,StreamingHttpResponse
from my_web import models
from django.utils.encoding import escape_uri_path
from cloud_disk import forms
import os
from My_First_Web.settings import BASE_DIR
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

per_page = 5

# Create your views here.
def cloud_index(request):
    if request.session.get('is_login',None):
        user = models.Customer.objects.get(id=request.session.get('id'))
        user_files = models.Cloud_Disk.objects.filter(customer = user)
        # file = user_files[0]
        # print(user_files)
        paginator = Paginator(user_files,per_page)
        page = request.GET.get('page')
        try:
            user_files = paginator.page(page)
        except PageNotAnInteger:
            user_files = paginator.page(1)
        except EmptyPage:
            user_files = paginator.page(paginator.num_pages)

    return render(request,"cloud_index/cloud_index.html",locals())

def add(request):
    customer = models.Customer.objects.get(id=request.session.get('id'))
    if request.method == "POST":
        print(dir(request.FILES))
        path = os.path.join(BASE_DIR,'data',str(customer.phone))
        path = "%s/data/%s/"%(BASE_DIR,str(customer.phone))

        if not os.path.isdir(path):
            os.makedirs(path,exist_ok=True)

        for k,file_obj in request.FILES.items():
            file_path = "%s/%s"%(path,file_obj.name)
            with open(file_path,'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
            cloud_disk = models.Cloud_Disk()
            cloud_disk.file = file_path
            cloud_disk.customer = customer
            cloud_disk.file_name = file_obj.name
            cloud_disk.save()
    return render(request,"cloud_index/cloud_add.html",locals())

def download_file(request,file_id):
    file = models.Cloud_Disk.objects.get(id=file_id)
    file_name = file.file.path
    # print("-------------",file_name)
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    response_name = str(file.file.name.split('/')[-1])
    response = StreamingHttpResponse(file_iterator(file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachement;filename="{0}"'.format(escape_uri_path(response_name))
    return response

def delete(request,file_id):
    file = models.Cloud_Disk.objects.get(id=file_id)
    file.delete()
    return redirect("/cloud_disk/")