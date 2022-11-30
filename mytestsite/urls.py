from django.contrib import admin
from django.urls import path

from main.views import test_view, current_time, workdir

menu = ['Главая страница', 'Время', '']
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', test_view, name='testview'),
    path('current_time/', current_time, name='time'),
    path('workdir/', workdir, name='workdir')


]
