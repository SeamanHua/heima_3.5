from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


'''
session 把状态保持的信息保存在了服务器上，他依赖于cookie。
第一次客户端向服务器发送请求时【请求头】没有携带任何信息，这时服务器会自动设置一个session的cookie信息保存在mysql或者是redis中，
在【响应头】中可以查看到。同时客户端收到响应后会保存session的cookie信息。
第二次操作时请求头中会携带session信息，服务器接收到后会和数据库中的session_key信息对比.一致则获取数据。
'''
def set_session(request):

    username = request.GET.get('username')  #得到用户访问时携带的信息username

    request.session['username'] = username  #设置session的cookie，这里不固定也可以是别的。

    # 设置session的过期时间
    # ① 默认是2周: set_expiry(None)
    # ② 设置: set_expiry( seconds ) seconds为秒
    request.session.set_expiry(3600)

    return HttpResponse('set_session')

def get_session(request):
    '''
    获取session
    第一种：username = request.session['username']
    第二种：username = request.session.get('username')

    删除
    del request.session['username']
    删除 session数据，但是sessionid保留
    request.session.clear()
    删除 session数据，同时 sessionid也删除
    request.session.flush()
    '''

    return HttpResponse('get_session')


'''
通过request.method来区分是GET请求还是POST请求，
根据不同的请求方式来实现不同的业务逻辑
下面是面向过程的方式：
'''
def test(request):
    if request.method == 'GET':
        return HttpResponse('get')
    else:
        return HttpResponse('post')


# TODO 类视图继承自View 面向对象的方式：
"""
定义一个  显示登录并实现登录的类视图：
class Name(View):
        
    def http_method_lower(self,request):
        
        return 响应
"""
from django.views import View

class JdLonginView(View):

    #实现相应的请求和响应
    def get(self,request):
        return HttpResponse('显示登录界面')

    def post(self,request):
        return HttpResponse('实现登录功能')

"""
定义一个 《个人中心》的类视图
类视图中有get方法用来获取数据；post方法用来修改数据
必须用户登录之后才可以访问，我们可以通过哪些方法实现：
① 装饰器可以实现对每个函数进行判断
② python的多继承可以实现：
系统提供了一个是否登录的判断：
from django.contrib.auth.mixins import LoginRequiredMixin
"""
from django.contrib.auth.mixins import LoginRequiredMixin

class CenterView(LoginRequiredMixin,View):   
    def get(self,request):
        return HttpResponse('center get')

    def post(self,request):
        return HttpResponse('post')