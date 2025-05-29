from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    content = {
        'name': 'Grimmjow'
    }
    return render(request, 'home.html', content)
