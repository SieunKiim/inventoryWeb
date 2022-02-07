from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from inven.models import User, Tool, Computer, Screen, Medical, Others


def index(request):
    context = {

    }
    return render(request, 'index.html', context=context)  # index.html에 넘겨줄 떄 같이 넘어갈 context 지정


def all(request):  # 모든 장비 조회
    tools = Tool.objects.all()
    tool_list = []
    for index_all, tool in enumerate(tools, start=1):
        tool_list.append(
            {'id': index_all,
             'user': tool.user.name,
             'tool_type': tool.tool_name,
             '부서': tool.user.department
             })
    return JsonResponse(tool_list, safe=False)


def computer(request):  # 컴퓨터 장비 조회
    computers = Computer.objects.all()
    computer_list = []
    for index_com, computer_each in enumerate(computers, start=1):
        computer_list.append({
            'user': computer_each.tool.user.name,  # 사용자
            'department': computer_each.tool.user.department,  # 부서
            'position': computer_each.tool.user.position,  # 직책
            'OS': computer_each.OS,
            'CPU': computer_each.CPU,
            'RAM': computer_each.RAM,
            'VGA': computer_each.VGA,
            'SSD_HDD': computer_each.SSD_HDD
        })
    return JsonResponse(computer_list, safe=False)


def screen(request):  # 화면 장비 조회 (모니터/티비)
    screens = Screen.objects.all()
    screen_list = []
    for index_screen, screen_each in enumerate(screens, start=1):
        screen_list.append({
            'user': screen_each.tool.user.name,  # 사용자
            'department': screen_each.tool.user.department,  # 부서
            'position': screen_each.tool.user.position,  # 직책
            'size': screen_each.size,  # 크기 (inch)
            'brand': screen_each.brand,  # 브랜드
            'resolution': screen_each.resolution  # 해상도
        })
    return JsonResponse(screen_list, safe=False)


def medical(request):  # 의료 장비 조회
    medicals = Medical.objects.all()
    medicals_list = []
    for index_medical, medical_each in enumerate(medicals, start=1):
        medicals_list.append({
            'user': medical_each.tool.user.name,  # 사용자
            'department': medical_each.tool.user.department,  # 부서
            'position': medical_each.tool.user.position,  # 직책
            'medical_type': medical_each.medical_type,  # 의료 기기 종류
            'serial_Number': medical_each.serial_Number,  # 시리얼 넘버
            'details': medical_each.details,  # 세부 정보
            'man_date': medical_each.man_date  # 생산 년도
        })
    return JsonResponse(medicals_list, safe=False)


def others(request):  # 기타 장비 조회
    other_tool = Others.objects.all()
    others_list = []
    for index_others, other in enumerate(other_tool, start=1):
        others_list.append({
            'user': other.tool.user.name,  # 사용자
            'department': other.tool.user.department,  # 부서
            'position': other.tool.user.position,  # 직책
            'other_tool_name': other.other_tool_name,  # 장비 종류
            'details': other.details  # 세부 사항
        })
    return JsonResponse(others_list, safe=False)


def inven_user(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'InvenUsers.html', context=context)


def add_user(request):  # 사용자 추가
    if request.method == 'POST':
        print("등록 POST")
    context = {

    }
    return render(request, 'add_user.html')
