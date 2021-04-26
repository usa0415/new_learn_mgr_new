from django.urls import path
from . import views

app_name = 'ioput'

urlpatterns = [
    path('', views.index, name='index'),
    path('page1/', views.input, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('alldata/', views.alldata, name='alldata'),
    path('page3/', views.page3, name='page3'),
]