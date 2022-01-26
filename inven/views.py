from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from inven.models import User, Tool, Computer, Screen


def index(request):
    context = {

    }
    return render(request, 'index.html', context=context)  # index.html에 넘겨줄 떄 같이 넘어갈 context 지정


def all(request):  # 모든 장비 조회
    # tools = Tool.objects.all()
    # context = {
    #     'tools': tools
    # }
    # return render(request, 'All.html', context)

    # users = User.objects.all()
    # user_list = []
    # for index_all, user in enumerate(users, start=1):
    #     user_list.append({'id': index_all, 'user': user.name, '부서': user.department})
    # return JsonResponse(user_list, safe=False)

    tools = Tool.objects.all()
    tool_list = []
    for index_all, tool in enumerate(tools, start=1):
        tool_list.append(
            {'id': index_all, 'user': tool.user.name, 'tool type': tool.tool_name, '부서': tool.user.department})
    return JsonResponse(tool_list, safe=False)


def computer(request):
    # computer_list = Computer.objects.all()
    # context = {
    #     'computer_list': computer_list
    # }
    # return render(request, 'Computer.html', context)

    computers = Computer.objects.all()
    computer_list = []
    for index_com, computer in enumerate(computers, start=1):
        computer_list.append({'id': index_com, 'user': computer.tool.user.name, 'department': computer.tool.user.department})
    return JsonResponse(computer_list, safe=False)


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


def inven_user(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'InvenUsers.html', context=context)


def others2(request):
    tools = Tool.objects.all()
    tool_list = []
    for index_all, tool in enumerate(tools, start=1):
        tool_list.append({'id': index_all, 'user': tool.tool_name, '부서': tool.user.department})
    return JsonResponse(tool_list, safe=False)


def add_user(request):
    if request.method == 'POST':
        print("등록 POST")
    context = {

    }
    return render(request, 'add_user.html')
