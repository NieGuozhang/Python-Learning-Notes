# -*- coding: UTF-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from mysite import models, forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.mail import EmailMessage


def index(request, pid=None, del_pass=None):
    # posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    # moods = models.Mood.objects.all()
    # try:
    #     user_id = request.GET['user_id']
    #     user_pass = request.GET['user_pass']
    #     user_post = request.GET['user_post']
    #     user_mood = request.GET['mood']
    # except:
    #     user_id = None
    #     message = '如果要张贴信息，那么每一个字段都要填...'
    #
    # if del_pass and pid:
    #     try:
    #         post = models.Post.objects.get(id=pid)
    #     except:
    #         post = None
    #
    #     if post:
    #         if post.del_pass == del_pass:
    #             post.delete()
    #             message = '数据删除成功'
    #         else:
    #             message = '密码错误'
    #
    # elif user_id != None:
    #     mood = models.Mood.objects.get(status=user_mood)
    #     post = models.Post.objects.create(mood=mood, nickname=user_id,
    #                                       message=user_post, del_pass=user_pass)
    #     post.save()
    #     message = '成功保存！请记得你的编辑密码[{}]!,信息须经审查后才会显示。'.format(user_pass)
    # if 'user_name' in request.session:
    #     username = request.session['user_name']
    #     useremail = request.session['useremail']
    #     message = 'cookie supported'
    # else:
    #     message = 'cookie not supported'
    # request.session.set_test_cookie()
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        try:
            user = auth.models.User.objects.get(username=username)
            diaries = models.Diary.objects.filter(user=user).order_by('-ddate')
        except:
            pass
    messages.get_messages(request)
    return render(request, 'index.html', locals())


def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'listing.html', locals())


@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)

    if request.method == 'POST':
        user = auth.models.User.objects.get(username=username)
        diary = models.Diary(user=user)
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, "日记已存储")
            post_form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.add_message(request, messages.INFO, '如果要张贴信息，那么每一个字段都要填...')
    else:
        post_form = forms.DiaryForm()
        messages.add_message(request, messages.INFO, '如果要张贴日记，每一个字段都要填...')
    return render(request, 'posting.html', locals())


def contact(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感谢您的来信"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']

            mail_body = u'''
            name：{}
            city：{}
            isSchool：{}
            Suggestions：如下
            {}'''.format(user_name, user_city, user_school, user_message)

            email = EmailMessage('来自【不吐不快】网站的网友意见', mail_body, user_email,
                                 ['nieguozhang@whut.edu.cn'])
            email.send()
        else:
            message = "请检查你输入的信息是否准确！"
    else:
        form = forms.ContactForm()
    return render(request, 'contact.html', locals())


def post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = '你的信息已保存，要等管理员启用后才看得到。'
            post_form.save()
            return HttpResponseRedirect(reverse('list'))
        else:
            message = '如果要张贴信息，那么每一个字段都要填...'
    else:
        post_form = forms.PostForm()
        message = '如果要张贴信息，那么每一个字段都要填...'
    return render(request, 'post2db.html', locals())


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS, '成功登录了')
                return redirect(reverse('index'))
            else:
                messages.add_message(request, messages.WARNING, '登录失败！')
                # messages.add_message(request, messages.WARNING, '密码错误，请再检查一次！')
        else:
            messages.add_message(request, messages.INFO, '请检查输入的字段内容')
    else:
        login_form = forms.LoginForm()

    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, '成功注销了')
    return redirect(reverse('index'))


@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        # print(request.user.is_authenticated)
        username = request.user.username
    user = User.objects.get(username=username)
    try:
        # print(user, 'user')
        profile = models.Profile.objects.get(user=user)
        # userinfo = models.Profile.objects.get(user=user)
        # print(userinfo, 'userinfo')
    except:
        profile = models.Profile(user=user)
    # if 'user_name' in request.session:
    #     username = request.session['user_name']
    # else:
    #     return redirect(reverse('login'))
    #
    # try:
    #     userinfo = models.User.objects.get(name=username)
    # except:
    #     pass
    # template = get_template('userinfo.html')
    # html = template.render(locals())
    # return render(request, 'userinfo.html', locals())
    if request.method == 'POST':
        profile_form = forms.ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            messages.add_message(request, messages.INFO, '个人资料已存储')
            profile_form.save()
            return HttpResponseRedirect(reverse('userinfo'))
        else:
            messages.add_message(request, messages.INFO, '要修改个人资料，每一个字段都要填...')
    else:
        profile_form = forms.ProfileForm()
    return render(request, 'userinfo.html', locals())
