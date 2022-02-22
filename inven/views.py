from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def add_user(request):  # 사용자 추가
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        position = request.POST['position']

        users = User(
            name=name,
            department=department,
            position=position
        )
        users.save()

        # 올바르다면 추가 + 추가 됐음을 알리는 alarm
        # 잘못 됐다면 오류 처리
    # return render(request, '../All/')
    return redirect('http://localhost:8080/inven/All/')


@csrf_exempt
def addComputer(request):  # 컴퓨터 추가
    if request.method == 'POST':
        user = request.POST['User']
        tool_name = request.POST['tool']
        os = request.POST['OS']
        cpu = request.POST['CPU']
        ram = request.POST['RAM']
        vga = request.POST['VGA']
        ssd_hdd = request.POST['SSD_HDD']

        # 입력하고자 하는 사용자가 존재하지 않을 때
        if not User.objects.filter(name=user).exists():
            messages.warning(request, "사용자 없음")
            print("사용자 없음")
            msg = "<h1>존재하지 않는 사용쟈</h1> \n 뒤로 가서 사용자를 먼저 추가해주세요"
            return HttpResponse(msg)

        else:
            tool = Tool(
                tool_name=tool_name,
                user=User.objects.get(name=user)
            )
            tool.save()

            computer = Computer(
                tool=tool,
                OS=os,
                CPU=cpu,
                RAM=ram,
                VGA=vga,
                SSD_HDD=ssd_hdd,
            )
            computer.save()

            return redirect('http://localhost:8080/inven/Computer/')
            # return JsonResponse(request.POST, safe=False)
    else:  # request.method = GET
        get_users = User.objects.all()
        user_list = []
        for index_users, user in enumerate(get_users, start=1):
            user_list.append({
                'name': user.name,
                'department': user.department
            })
        return JsonResponse(user_list, safe=False)


@csrf_exempt
def addScreen(request):  # 스크린 추가
    if request.method == 'POST':
        # print(request.POST)
        user = request.POST['User']
        tool_name = request.POST['tool']
        size = request.POST['size']
        brand = request.POST['brand']
        resolution = request.POST['resolution']

        # 입력하고자 하는 사용자가 존재하지 않을 때
        if not User.objects.filter(name=user).exists():
            messages.warning(request, "사용자 없음")
            print("사용자 없음")
            msg = "<h1>존재하지 않는 사용쟈</h1> \n 뒤로 가서 사용자를 먼저 추가해주세요"
            return HttpResponse(msg)

        else:
            tool = Tool(
                tool_name=tool_name,
                user=User.objects.get(name=user)
            )
            tool.save()

            screen_to_add = Screen(
                tool=tool,
                size=size,
                brand=brand,
                resolution=resolution
            )
            screen_to_add.save()

            return redirect('http://localhost:8080/inven/Screen/')
            # return JsonResponse(request.POST, safe=False)
    else:  # request.method = GET
        get_users = User.objects.all()
        user_list = []
        for index_users, user in enumerate(get_users, start=1):
            user_list.append({
                'name': user.name,
                'department': user.department
            })
        return JsonResponse(user_list, safe=False)


@csrf_exempt
def addOthers(request):  # 기타 장비 추가
    # 툴 네임이 툴로 저장되야하는게 맞을거야
    print(request.POST)
    if request.method == 'POST':
        user = request.POST['User']
        tool_name = request.POST['tool']
        other_tool_name = request.POST['other_tool_name']
        details = request.POST['details']

        # 입력하고자 하는 사용자가 존재하지 않을 때
        if not User.objects.filter(name=user).exists():

            messages.warning(request, "사용자 없음")
            print("사용자 없음")
            msg = "<h1>존재하지 않는 사용자</h1> \n 뒤로 가서 사용자를 먼저 추가해주세요"
            return HttpResponse(msg)

        else:
            tool = Tool(
                tool_name=other_tool_name,
                user=User.objects.get(name=user)
            )
            tool.save()

            others_to_add = Others(
                tool=tool,
                other_tool_name=other_tool_name,
                details=details

            )
            others_to_add.save()

            return redirect('http://localhost:8080/inven/Others/')
            # return JsonResponse(request.POST, safe=False)
    else:  # request.method = GET
        get_users = User.objects.all()
        user_list = []
        for index_users, user in enumerate(get_users, start=1):
            user_list.append({
                'name': user.name,
                'department': user.department
            })
        return JsonResponse(user_list, safe=False)


@csrf_exempt
def addMedical(request):  # 의료 기기 추가
    if request.method == 'POST':
        # print(request.POST)
        user = request.POST['User']
        tool_name = request.POST['tool']
        medical_type = request.POST['medical_type']
        details = request.POST['details']
        serial_Number = request.POST['serial_Number']
        man_date = request.POST['man_date']

        # 입력하고자 하는 사용자가 존재하지 않을 때
        if not User.objects.filter(name=user).exists():
            messages.warning(request, "사용자 없음")
            print("사용자 없음")
            msg = "<h1>존재하지 않는 사용쟈</h1> \n 뒤로 가서 사용자를 먼저 추가해주세요"
            return HttpResponse(msg)

        else:
            tool = Tool(
                tool_name=tool_name,
                user=User.objects.get(name=user)
            )
            tool.save()

            medical_to_add = Medical(
                tool=tool,
                medical_type=medical_type,
                details=details,
                serial_Number=serial_Number,
                man_date=man_date
            )
            medical_to_add.save()

            return redirect('http://localhost:8080/inven/Medical/')
            # return JsonResponse(request.POST, safe=False)
    else:  # request.method = GET
        get_users = User.objects.all()
        user_list = []
        for index_users, user in enumerate(get_users, start=1):
            user_list.append({
                'name': user.name,
                'department': user.department
            })
        return JsonResponse(user_list, safe=False)
