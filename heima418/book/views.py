from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request):

    return HttpResponse('ok')

def register(request,mobile):
    return HttpResponse('自定义验证码成功！')


def shop(request,pro_id,city_id):

    # TODO 1.GET请求--Url路径参数
    print(pro_id,city_id)

    # TODO 2.查询字符串
    # http: // ip: port / uri /?key = value & key2 = value2
    # 以问好（？）为分隔符
    # ？前边为我们访问的url
    # http: // ip: port / uri /
    # ?后边为查询字符串
    # key = value & key2 = value2
    # 查询字符串是以 & 作为分隔的
    #用 resquest.GET 获取查询字符串的数据
    query_params = request.GET
    print(query_params)
    # TODO 2.1 查询字典对象
    alist = query_params.getlist('a')  #获取一键多值
    print(alist)
    asingle = query_params.get('a')    #获取一键一值，这个值是最后一个
    print('-------------')
    print(asingle)

    return HttpResponse('我的后宫三千')

# TODO 3.POST请求--表单类型From Data
def login(request):
    #通过request.POST就可以获取表单数据
    data = request.POST
    print(data)
    return HttpResponse('login')

# TODO 3.1 非表单类型Non-From Data（json数据）
def weibo(request):
    #JSON数据的接收是在request.body中
    #1.接收数据   结果为bytes类型
    body = request.body
    print(body)

    #2.将接收的bytes类型的数据转换为str类型
    body_str = body.decode()
    print(body_str)

    """
    body_str是json形式的字符串，不是字典类型
    所以要转换为字典的类型
    {
        "username":"zhangzhenhua",
        "password":"1234567"    
    }
    
    """

    #3.将字符串转换为字典
    import json
    data = json.loads(body_str)
    print(data)

    return HttpResponse('weibo json')

# TODO 4 请求头
def get_header_info(request):
    print(request.META)  #得到的是字典类型的数据

    print('--------------')
    print(request.META['CONTENT_TYPE'])

    return HttpResponse('header')



# TODO HttpResponse
from django.http.response import HttpResponse
from django.http import HttpResponse
def http_res(request):
    # content 响应体的内容，可以是 str,int,list,dict，不能是对象。
    # content_type是响应体数据类型 告诉浏览器 我返回的是什么数据
    # 语法形式: '大类/小类' 例如: 'text/html'
    # status=状态码
    # 1xx , 消息
    # 2xx,  成功
    # 3xx,  重定向
    # 4xx,  请求错误
    # 5xx   服务器错误
    # HTTP status code must be an integer from 100 to 599.
    return HttpResponse('abc',status=200,content_type='text/html')

# TODO JsonResponse
from django.http.response import JsonResponse

def res_json(request):
    # JSON 数据和python的字典很像

    data = {
        'name':'heima',
        'age':17
    }
    #  JsonResponse的第一个参数data,要求数据格式为字典类型.
    import json
    data_str = json.dumps(data)
    """
    如果我们的 data 不是字典数据, 这个时候,我们可以通过修改 safe=False 来让系统进行转换
    return JsonResponse(data,safe=False)
    """

    return JsonResponse(data_str,content_type='application/json')




# 实现状态保持主要有两种方式：
# 在客户端存储信息使用 Cookie
# 在服务器端存储信息使用 Session

#TODO Cookie   cookie在响应头里面
def set_cookie(request):

    username = request.GET.get('username')

    response = HttpResponse('set_cookie')

    # cookie数据的设置会保存在响应头中,所以要操作响应对象,
    # max_age就是从现在起设计的一个定时秒数也就是过期时间。浏览器默认为0,不进行保存。
    response.set_cookie(key='name',value=username,max_age=100)


    return response

#第二次请求
def get_cookie(request):

    username = request.COOKIES.get('name')

    print(username)


    return HttpResponse('get_cookie')










