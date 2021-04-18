from django.urls import path
from book.views import index,shop,login,weibo,get_header_info,register,set_cookie,get_cookie

# 为了验证数据是否符合规范，系统提供了转换器，必须在urls下使用
# <转换器名字：变量名>
from django.urls.converters import IntConverter


#  1.自定义转换器
class MobileConventer:
    #正则
    regex = '1[3-9]\d{9}'

    def to_python(selfs,value):
        return value

# 2.把定义的转换器注册给系统
from django.urls.converters import register_converter

# 给定义的转换器起名字
register_converter(MobileConventer,'nn')



urlpatterns = [
    path('index/',index),

    #3.使用
    path('register/<nn:mobile>/',register),

    # <>起到了占位的作用，用于请求路径的方式
    path('<int:pro_id>/<int:city_id>/',shop),

    path('login/',login),

    path('weibo/',weibo),

    path('header/',get_header_info),

    path('set_cookie/',set_cookie),

    path('get_cookie/',get_cookie)

]