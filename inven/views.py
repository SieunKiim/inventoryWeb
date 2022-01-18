from django.shortcuts import render


# Create your views here.
from inven.models import User


def index(request):
    context = {

    }
    return render(request, 'index.html', context=context)  # index.html에 넘겨줄 떄 같이 넘어갈 context 지정


def All(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list
    }
    print(len(user_list))
    return render(request, 'All.html', context)


def Computer(request):
    context = {

    }
    return render(request, 'Computer.html', context=context)


def Screen(request):
    context = {

    }
    return render(request, 'Screen.html', context=context)


def Medical(request):
    context = {

    }
    return render(request, 'Medical.html', context=context)


def others1(request):
    context = {

    }
    return render(request, 'others1.html', context=context)


def others2(request):
    context = {

    }
    return render(request, 'others2.html', context=context)

#
# def user(request): # 모든 유저가 사용하는 장비 조회
#     return User.objects.all()
