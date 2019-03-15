from django.shortcuts import render
from spider.task.pachong import get_data
from django.http import HttpResponse
import json
# Create your views here.
def spider_index(request):
    pages = 1
    results = []
    if request.method == "GET":
        search_key = request.GET.get('search')

        if search_key:
            results = get_data(search_key,pages=pages)
    if request.method == "POST":
        if request.is_ajax():
            search_key = request.POST.get("search_key")
            pages = int(request.POST.get("pages"))
            print(search_key,pages)
            try:
                results = get_data(search_key, pages=pages)
                return HttpResponse(json.dumps(results))
            except:
                pass
    return render(request,"spider/spider.html",{"results":results})