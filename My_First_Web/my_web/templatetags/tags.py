from django import template
from django.utils.safestring import mark_safe
from django.utils.timezone import datetime,timedelta
from my_web.task.weather import get_weather

register = template.Library()

@register.simple_tag
def build_register(field):

    return field.name == "password"

@register.simple_tag
def build_weather():
    weathers = get_weather()
    return weathers

@register.simple_tag
def build_file_obj(file):
    ele = """<tr><td>{file_name}</td>
                <td>{file_size}K</td>
                <td>{file_time}</td>
                <td><a href="/cloud_disk/download/{file_id}/"><span class="glyphicon glyphicon-arrow-down"></span></a></td>
                <td><a href="/cloud_disk/delete/{file_id}/" onClick="return confirm('确定删除?');"><span class="glyphicon glyphicon-remove"></span></a></td>
             </tr>"""
    # print(files)
    file_id = file.id
    file_name = file.file.name.split("/")[-1]
    # file_name = file.file.name
    file_size = file.file.size / 1024
    file_size = format(file_size,"0.2f")
    file_time = file.create_time.strftime("%Y-%m-%d %H:%M:%S")
    ele = ele.format(file_name=file_name,file_size=file_size,file_time=file_time,file_id = file_id)
    # print(file_name,file_size,file_time)
    return mark_safe(ele)

@register.simple_tag
def build_log_context(log_context):
    ele = str(log_context)
    return ele[0:80]

@register.simple_tag
def build_paginator( objs ):
    add_dot_ele = False
    ele = ''
    for page_number in objs.paginator.page_range:
        if page_number<3 or page_number > objs.paginator.num_pages-2 or abs(page_number-objs.number) < 2:
            if page_number == objs.number:
                add_dot_ele = False
                ele +='<li class="active"><a href="?page=%s">%s</a></li>'%(page_number,page_number)
            else:
                ele += '<li class=""><a href="?page=%s">%s</a></li>' % (page_number, page_number)
        else:
            if add_dot_ele == False:
                ele += '<li class=""><a >...</a></li>'
                add_dot_ele = True
    return mark_safe(ele)

@register.filter
def layout(a,b):
    b,c = b.split(",")
    b = int(b)
    c = int(c)
    if a % b == c :
        return True
    return False

@register.filter
def is_Tag (label_tag,key):
    # print(dir(label_tag))
    # print(label_tag,key)
    if label_tag == key:
        return True
    return False