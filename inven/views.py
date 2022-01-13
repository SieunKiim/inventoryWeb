from django.shortcuts import render


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context=context)  # index.html에 넘겨줄 떄 같이 넘어갈 context 지정
