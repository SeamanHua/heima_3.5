# 中间件：在Django处理视图的不同阶段对输入或输出进行干预，当我们在处理 请求 和响应的时候 会伴随发送的
# 在请求视图被处理前，中间件由上至下依次执行
# 在请求视图被处理后，中间件由下至上依次执行

from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(MiddlewareMixin):
    #每次请求前都会调用执行
    def process_request(self,request):
        print('process_request')

        # TODO  用途 中间件可以在请求前判断用户是否为登录用户
        user = request.COOKIES.get('user')
        if user is not None:
            print('用户登录')
        else:
            print('游客登录')

    #每次响应后（视图）都会调用执行
    def process_response(self,request,response):
        print('process_response')

        # TODO 用途 可以设置响应头提高安全性
        response['Server'] = 'xxxxxx'

        return response


