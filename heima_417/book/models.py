from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """
    id              主键
    name            书籍名字
    pub_date        书籍发布日期
    readcount       阅读量
    commentcount    评论量
    is_delete       是否删除
    """
    name = models.CharField(max_length=10)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    #固定写法,修改表名
    class Meta:
        db_table = 'bookinfo'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0,'male'),
        (1,'female')
    )

    name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    is_delete = models.BooleanField(default=False)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0)



    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name
