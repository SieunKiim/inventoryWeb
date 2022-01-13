from django.shortcuts import render


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context=context)  # index.html에 넘겨줄 떄 같이 넘어갈 context 지정


def All(request):
    context = {

    }
    return render(request, 'All.html', context=context)


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