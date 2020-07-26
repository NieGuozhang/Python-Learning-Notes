from django.shortcuts import render
from PIL import Image
from .models import User


# Create your views here.
def index_unlog(request):
    return render(request, 'blog/index_unlog.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = User.objects.filter(username=user_name)  # 查看数据库里是否有该用户名
        if user:  # 如果存在
            user = User.objects.get(username=user_name)  # 读取该用户信息
            if pass_word == user.password:  # 检查密码是否匹配
                request.session['IS_LOGIN'] = True
                request.session['nickname'] = user.nickname
                request.session['username'] = user_name
                return render(request, 'blog/index.html', {'user': user})
            else:
                return render(request, 'blog/login.html', {'error': '密码错误!'})
        else:
            return render(request, 'blog/login.html', {'error': '用户名不存在!'})
    else:
        return render(request, 'blog/login.html')


def logsuccess(request):
    return render(request, 'blog/index.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        password_1 = request.POST.get('password_1', '')
        password_2 = request.POST.get('password_2', '')
        nickname = request.POST.get('nickname', '')
        email = request.POST.get('email', '')
        avatar = request.FILES.get('avatar')
        if User.objects.filter(username=user_name):
            return render(request, 'blog/register,html', {'error': '用户已存在'})
            # 将表单写入数据库
        if (password_1 != password_2):
            return render(request, 'register.html', {'error': '两次密码请输入一致'})

        user = User()
        # if avatar:
        #     print(avatar)
        #     user.avatar = 'media/' + user_name + '.jpg'
        #     img = Image.open(avatar)
        #     size = img.size
        #     print(size)
        #     # 因为是要圆形，所以需要正方形的图片
        #     r2 = min(size[0], size[1])
        #     if size[0] != size[1]:
        #         img = img.resize((r2, r2), Image.ANTIALIAS)
        #     # 最后生成圆的半径
        #     r3 = int(r2 / 2)
        #     img_circle = Image.new('RGBA', (r3 * 2, r3 * 2), (255, 255, 255, 0))
        #     pima = img.load()  # 像素的访问对象
        #     pimb = img_circle.load()
        #     r = float(r2 / 2)  # 圆心横坐标
        #     for i in range(r2):
        #         for j in range(r2):
        #             lx = abs(i - r)  # 到圆心距离的横坐标
        #             ly = abs(j - r)  # 到圆心距离的纵坐标
        #             l = (pow(lx, 2) + pow(ly, 2)) ** 0.5  # 三角函数 半径
        #
        #             if l < r3:
        #                 pimb[i - (r - r3), j - (r - r3)] = pima[i, j]
        #     img_circle.save('blog/static/media/' + user_name + '.jpg')

        user.username = user_name
        user.password = password_1
        user.email = email
        user.nickname = nickname
        user.save()
        # 返回注册成功页面
        return render(request, 'blog/login.html')
    else:
        return render(request, 'blog/register.html')


def forget_password(request):
    if request.method == "POST":
        user_name = request.POST.get('username', '')
        email = request.POST.get('email', '')
        user = User.objects.filter(username=user_name)
        if user:
            user = User.objects.get(username=user_name)
            if user.email == email:
                request.session['user_name'] = user_name
                return render(request, 'blog/reset.html')
            else:
                return render(request, 'blog/forget.html', {'error': '您的用户名和邮箱不匹配！'})
        else:
            return render(request, 'blog/forget.html', {'error': '请输入正确的用户名'})
    else:
        return render(request, 'blog/forget.html')


def reset(request):
    if request.method == 'POST':
        pass_word1 = request.POST.get('password1', '')
        pass_word2 = request.POST.get('password2', '')
        user_name = request.session['user_name']
        user = User.objects.get(username=user_name)
        if pass_word1 == pass_word2:
            user.password = pass_word1
            user.save()
            return render(request, 'blog/login.html')
        else:
            return render(request, 'blog/reset.html', {'error': '两次密码输入不一致！'})
    else:
        return render(request, 'blog/reset.html')
