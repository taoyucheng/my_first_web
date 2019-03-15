from django.shortcuts import render,redirect
from my_web import forms
from my_web import models
from my_web.task.hs_password import hash_code
from django.views.decorators.csrf import csrf_exempt,csrf_protect



# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        if request.is_ajax():
            # print(request.POST.get("username"))
            # print(request.POST.get("password"))
            pass
    # return render(request,"Vue/test01.html")
    return render(request,"index.html")

def login(request):
    if request.session.get('is_login',None):
        return redirect("/")
    if request.method == "POST":
        login_form = forms.Userform(request.POST)
        message = "请检查填写内容"

        if login_form.is_valid():
            phone = login_form.cleaned_data['phone']
            password = login_form.cleaned_data['password']
            print(phone,password)
            print(models.Customer.objects.first())
            try:
                user = models.Customer.objects.get(phone = phone)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_name'] = user.name
                    request.session['id'] = user.id

                    return redirect("/")
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'my_web/login.html', locals())

    login_form = forms.Userform()
    return render(request,'my_web/login.html',locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/")
    request.session.flush()
    return redirect("/")

def register(request):
    if request.session.get('is_login',None):
        return redirect("/")

    if request.method == "POST":
        user_form = forms.CustomerForm(request.POST)
        message = "请检查填写内容！"
        print(user_form.is_valid())
        print(user_form.errors)
        if user_form.is_valid():
            password = request.POST.get('password-repeat')
            user = models.Customer.objects.filter(phone=user_form.cleaned_data['phone'])
            if password == user_form.cleaned_data['password']:
                if user:
                    message = "用户已存在！"
                    return render(request, "my_web/register.html", locals())
                else:
                    user = models.Customer()
                    user.name = user_form.cleaned_data['name']
                    user.phone = user_form.cleaned_data['phone']
                    user.password = hash_code(password)
                    user.sex = user_form.cleaned_data['sex']
                    user.address = user_form.cleaned_data['address']
                    user.birthday= user_form.cleaned_data['birthday']

                    user.save()

                    return redirect("/login/")
            else:
                message = "两次密码不一致！"
                # register_form = user_form
                # register_form.password = ""
                return render(request, "my_web/register.html", locals())
        else:
            message = "用户已存在"
    register_form = forms.CustomerForm()
    return render(request,"my_web/register.html",locals())
    # return redirect("/")

def changepwd(request,user_id):
    if request.method == "POST":
        print("______________________________")

        obj = models.Customer.objects.get(id=user_id)
        password_old = request.POST.get("password-old").strip()
        password_new1 = request.POST.get("password-new").strip()
        password_new2 = request.POST.get("password-new-repeat").strip()
        if obj.password == hash_code(password_old):
            if password_new1 != password_new2:
                message = "两次密码不一致！"
            else:
                obj.password = hash_code(password_new2)
                obj.save()
                request.session.flush()
                # print("______________________________")
                return redirect("/login/")
        else:
            message = "旧密码不正确！"

    return render(request, "my_web/changepassword.html", locals())

def changemsg(request,user_id):
    obj = models.Customer.objects.get(id=user_id)
    change_form = forms.CustomerChangeForm(instance=obj)
    if request.method == "POST":
        user_form = forms.CustomerChangeForm(request.POST)
        # print(user_form.errors)
        if user_form.is_valid():
                obj.name = user_form.cleaned_data['name']
                obj.sex = user_form.cleaned_data['sex']
                obj.address = user_form.cleaned_data['address']
                obj.birthday = user_form.cleaned_data['birthday']
                # print(user_form.cleaned_data['birthday'])
                # obj = user_form
                obj.save()
                # change_form = forms.CustomerChangeForm(instance=obj)
                return redirect("/logout/")
    return render(request, "my_web/changemsg.html", locals())

def blogs(request):
    return render(request,"my_web/blogs.html")