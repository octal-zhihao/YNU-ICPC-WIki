from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.utils import timezone
from Wiki.models.index import Profile, Article
import markdown
from django.http import HttpResponse #调试

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.lexers.python import PythonLexer

# Create your views here.
def index(request):
    return render(request, "index.html")


# 注册
def signup(request):
    # 如果是post请求
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # 如果密码相等
        if password == password2:
            # 如果邮箱已存在
            if User.objects.filter(email=email).exists():
                messages.info(request, " 邮箱已存在")
                return redirect('signup')
            # 如果用户名已经存在
            elif User.objects.filter(username=username).exists():
                messages.info(request, "用户名已经存在")
                return redirect('signup')
            # 如果都不存在
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # 登录
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                # 设置默认的个人信息
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                # 跳转到设置个人信息界面
                return redirect('index')
        # 如果密码不等，提示
        else:
            messages.info(request, '两次输入的密码不一致！')
            return redirect('signup')
    # 如果请求不是post，保持在注册界面
    else:
        return render(request, 'signup.html')

# 登录
def signin(request):
    # 如果是post请求
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # 校验
        user = auth.authenticate(username=username, password=password)
        # 如果用户存在
        if user is not None:
            # messages.info(request, '登录成功')
            # return redirect('signin')
            auth.login(request, user)
            return redirect('/')
        # 如果用户不存在
        else:
            messages.info(request, '登录失败')
            return redirect('signin')
    # 如果不是post请求
    else:
        return render(request, 'signin.html')
    
def start(request):
    articles = Article.objects.all()
    for article in articles:
        if article.title == "算法竞赛入门指南":
            article.content = markdown.markdown(article.content,
                extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.extra',
            ]) # 将Markdown转换为HTML
            return render(request, 'article.html', {'article' : article})

def stl(request):
    articles = Article.objects.all()
    for article in articles:
        if article.title == "C++ STL库":
            article.content = markdown.markdown(article.content,
                extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.extra',
            ]) # 将Markdown转换为HTML
            return render(request, 'article.html', {'article' : article})
        
def basic(request):
    articles = Article.objects.all()
    for article in articles:
        if article.title == "基础算法":
            article.content = markdown.markdown(article.content,
                extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.extra',
            ]) # 将Markdown转换为HTML
            return render(request, 'article.html', {'article' : article})
        
def advanced(request):
    articles = Article.objects.all()
    for article in articles:
        if article.title == "进阶算法":
            article.content = markdown.markdown(article.content,
                extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.extra',
            ]) # 将Markdown转换为HTML
            return render(request, 'article.html', {'article' : article})
