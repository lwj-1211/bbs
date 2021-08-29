from django.db.models import query
from django.shortcuts import render
from .models import TblUser

# Create your views here.

# 接收POST请求数据
def login_page(request):
    info ={}
    if request.POST:
        info['uname'] = request.POST['username']
        info['psword'] = request.POST['password']
        info["result"] = "没有这个用户"
        query_result = TblUser.objects.all()
        print(info)
        for user in query_result:
            if user.username == request.POST['username'] and \
               user.password == request.POST['password']:
                info["result"] = "有这个用户"
    return render(request, "login/login.html", info)
