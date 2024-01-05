from django.db import models
from django.contrib.auth import get_user_model
from mdeditor.fields import MDTextField
User = get_user_model()

class Profile(models.Model):
    # 当前操作的用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    # 个人介绍
    bio = models.TextField(blank=True)
    # 头像
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    # 地域
    location = models.CharField(max_length=100, blank=True)

# 文章表
class Article(models.Model):
    # 文章标题title
    title = models.CharField(max_length=64, verbose_name='标题')
    # 文章内容content
    content = MDTextField(default="", editable=True, blank=True, verbose_name='正文')
    article_picture = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.title  # 返回文章标题作为对象的字符串表示形式