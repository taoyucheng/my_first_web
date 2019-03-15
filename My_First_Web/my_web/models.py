from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64,null=True,blank=True,verbose_name='姓名')
    phone = models.CharField(max_length=64,unique=True,verbose_name='电话号码')
    password = models.CharField(max_length=128,verbose_name='密码')
    sex_choices = (('male','男'),
                   ('female','女'))
    sex = models.CharField(max_length=32,choices=sex_choices,default='男',verbose_name='性别')
    address = models.CharField(max_length=128,null=True,blank=True,verbose_name='家庭住址')
    birthday = models.DateField(null=True,blank=True,verbose_name='出生日期')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    # is_register = models.BooleanField(default=False)
    def __str__(self):
        return "%s-%s"%(self.name,self.phone)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"

def upload_to(instance,filename):
    return '/'.join(['data',instance.customer.phone,filename])

class Cloud_Disk(models.Model):
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE,verbose_name="用户名")
    file_name = models.CharField(max_length=256,null=True,blank=True,verbose_name="文件名")
    # file_size = models.CharField(max_length=128,null=True,blank=True,verbose_name="文件大小")
    file = models.FileField(upload_to=upload_to,verbose_name="文件地址")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    def __str__(self):
        return "%s-%s"%(self.file_name,self.create_time)

    class Meta:
        verbose_name = "云盘"
        verbose_name_plural = "云盘"

class Log(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name="用户名")
    log_head = models.CharField(max_length=256,null=True,blank=True)
    log_context = models.TextField(verbose_name="日志内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    def __str__(self):
        return self.log_head

    class Meta:
        verbose_name = "日志"
        verbose_name_plural = "日志"
