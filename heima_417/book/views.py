from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from book.models import BookInfo

def index(request):
     # 正常情况下下列修改数据的代码要写在此处，为了方便测试才写在外面！
    return HttpResponse('ok')


# TODO 增加数据方法一
book = BookInfo(          #1.创建实例对象
    name='Python高级',
    pub_date='2020-1-1'
)
book.save()  #2.保存


# TODO 增加数据方法二
book = BookInfo.objects.create(
    name = 'jango',
    pub_date='2020-2-2',
    readcount=666,
    commentcount=999
)


# TODO 更新数据方法一
book = BookInfo.objects.get(id=1)   #获取实例对象
book.name = '射雕英雄后传'            #通过设置实例对象的属性修改数据
book.readcount = 120
book.save()                         #人为的调用保存
# TODO 更新数据方法二
BookInfo.objects.filter(id=1).update(
    name = '射雕英雄前传',
    pub_date = '2020-1-2'
)


# TODO 删除数据方法一
book = BookInfo.objects.gets(id=1)
book.delete()
# TODO 删除数据方法二
BookInfo.objects.get(id=1).delete()
BookInfo.objects.filter(id=5).delete()


# TODO 查询操作
try:
    BookInfo.objects.get(id=1)
except Exception:
    print('没有查询到')
# 查询所有
BookInfo.objects.all()
# 查询所有数量
BookInfo.objects.all().count()

"""
where 语句
- filter过滤出多个结果 返回的是列表
- exclude排除掉符合条件剩下的结果
- get过滤单一结果  
以 filter为例
语法形式是:  filter(属性__运算符=值)
"""
# TODO 过滤查询
BookInfo.objects.filter(id__exact=2)  #返回的是列表，如果不存在不会报错
BookInfo.objects.get(id__exact=2)     #返回的是对象 ，如果不存在会报错
#查询编号为2的图书
BookInfo.objects.get(id=2)            #上面的id__exact是完整的写法
BookInfo.objects.filter(id=2)
#查询书名包含‘湖’的图书
BookInfo.objects.filter(name__contains='湖')
#查询书名以‘’部‘结尾的图书
BookInfo.objects.filter(name__endswith='部')
#查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
#查询编号为1或3或5的图书

'''
gt  大于  great
gte   大于等于 e equal 等于
lt  小于  less than  litte
lte  小于等于
'''
BookInfo.objects.filter(id__in=[1,3,5])
#查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
#查询1980年发表的图书
BookInfo.objects,filter(pub__date__year=1980)
#查询1990年一月一号发表的图书
BookInfo.objects.filter(pub_date__gte='1990-1-1')
#exclude 和 not一样查询id不等于3的
BookInfo.objects.exclude(id=3)


# TODO 查询--F对象，两个属性的比较
from django.db.models import F
#模型类名.objects.filter(属性名__运算符=F('属性名'))   查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount=F('commentcount'))
# 查询书籍id 大于2 并且 阅读量大于30的书籍,以下三种方法：
BookInfo.objects.filter(id__gt=2).filter(readcount__gt=30)
BookInfo.objects.filter(id__gt=2,readcount__gt=30)
from django.db.models import Q
# &         并且
# |         或者
# ~         非(not)  和 exclude 很类似
#语法形式:  Q(属性名__运算符=值)
BookInfo.objects.filter(Q(id__gt=2)&Q(readcount__gt=30))
# 查询书籍id 大于2 或者 阅读量大于30的书籍
BookInfo.objects.filter(Q(id__gt=2)|Q(readcount__gt=30))
# 查询编号不等于3的图书
# ~Q not 非 和exclude 类似
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))

# TODO 查询聚合函数
# 模型类名.objects.aggregate(Xxx('属性名'))   返回值为字典
from django.db.models import Sum,Max,Min,Avg,Count
BookInfo.objects.aggregate(Sum('readcount'))
#排序,默认升序，属性前加负号表示降序
BookInfo.objects.all().order_by('readcount')
BookInfo.objects.all().order_by('-readcount')

# TODO 查询关联查询
#由一到多的访问语句,根据书籍查找人物
book=BookInfo.objects.get(id=2)
book.peopleinfo_set.all()
#由多到一，根据人物查书籍
from book.models import PeopleInfo
people = PeopleInfo.objects.get(id=6)
people.book
# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name='郭靖')
BookInfo.objects.filter(peopleinfo__description__contains='八')
#查询图书阅读量大于30的人物
PeopleInfo.objects.filter(book__readcount__gt=30)
#查询书名为’天龙八部‘的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')


# TODO 分页
from django.core.paginator import Paginator

# 2. 组织列表数据
books=BookInfo.objects.all()
# 3. 创建分页对象
p = Paginator(books,per_page=2)     #per_page，每页多少条数据
# 4. 获取第几页数据
page_objects=p.page(1)
# 总共多少页
p.num_pages
# 要分页的数据
page_objects.object_list



