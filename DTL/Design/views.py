from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    content = {
        'name': 'Grimmjow'
    }
    return render(request, 'home.html', content)

def add(request):
    num1 = int(request.GET['number1'])
    num2 = int(request.GET['number2'])
    res = num1+num2
    return render(request, 'result.html',{'result':res})
