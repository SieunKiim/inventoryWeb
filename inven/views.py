from django.shortcuts import render

# Create your views here.
from inven.models import User, Tool, Computer, Screen


def index(request):
    context = {

    }
    return render(request, 'index.html', context=context)  # index.html에 넘겨줄 떄 같이 넘어갈 context 지정


def all(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list
    }
    print(len(user_list))
    return render(request, 'All.html', context)


def computer(request):
    computer_list = Computer.objects.all()
    context = {
        'computer_list': computer_list
    }
    return render(request, 'Computer.html', context)


def screen(request):
    screen_list = Screen.objects.all()
    context = {
        'screen_list': screen_list
    }
    return render(request, 'Screen.html', context)


def medical(request):
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


def add_user(request):
    if request.method == 'POST':
        print("등록 POST")
    context = {

    }
    return render(request, 'add_user.html')
