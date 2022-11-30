import datetime
from django.shortcuts import render
from django.http import HttpResponse

menu = ['Главая страница', 'Время', 'Содержимое сайта']

def test_view(request):
    return render(request, 'mytestsite/package.html', {'title': 'Главная страница'})

def current_time(request):
    return HttpResponse(f'Time = {datetime.datetime.now()},')

def  workdir(request):
    return render(request, 'mytestsite/workdir.html', {'menu': menu, 'title':'Содержимое сайта'})




