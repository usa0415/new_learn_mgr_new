from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import mark_safe
from .forms import inputform
from .models import leraning_time
from django.db.models import Sum

def alldata(request):
    return render(request, 'new_learn_mgr/alldata.html',{
        'leraning_time': leraning_time.objects.all().order_by('-id'),
    })

def index(request):
    category=[]
    time=[]
    day=[]

    #棒グラフ用データ
    queryset = leraning_time.objects.all().order_by('-id')[:7]
    for Leraning_time in queryset:
        category.append(Leraning_time.category)
        day.append(str(Leraning_time.day))
        time.append(Leraning_time.time)

    T1 = [0, 0, 0, 0, 0, 0]
    T2 = [0, 0, 0, 0, 0, 0]
    T3 = [0, 0, 0, 0, 0, 0]
    T4 = [0, 0, 0, 0, 0, 0]
    T5 = [0, 0, 0, 0, 0, 0]
    T6 = [0, 0, 0, 0, 0, 0]
    T7 = [0, 0, 0, 0, 0, 0]

    if len(time) > 0:
        T1.insert(0, time[0])
        T2.insert(1, time[1])
        T3.insert(2, time[2])
        T4.insert(3, time[3])
        T5.insert(4, time[4])
        T6.insert(5, time[5])
        T7.insert(6, time[6])

    if len(category) == 0:
        category = ['', '', '', '', '', '', '']

    #円グラフ用データ
    pie_data = leraning_time.objects.all().values('category').annotate(total=Sum('time'))
    pie_label = [x['category'] for x in pie_data]
    pie_data = [x['total'] for x in pie_data]

    Sum_time = leraning_time.objects.all().aggregate(Sum('time'))
    total_time = Sum_time['time__sum']

    return render(request, 'new_learn_mgr/index.html',{
        'C1':category[0],
        'C2':category[1],
        'C3':category[2],
        'C4':category[3],
        'C5':category[4],
        'C6':category[5],
        'C7':category[6],
        'category':category,
        'T1': T1,
        'T2': T2,
        'T3': T3,
        'T4': T4,
        'T5': T5,
        'T6': T6,
        'T7': T7,
        'time':time,
        'day':day,
        'pie_label':pie_label,
        'pie_data':pie_data,
        'total_time':total_time ,
    })

#実績一覧の表示とフォーム送信
def input(request):
    if request.method == 'POST':
        form = inputform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'new_learn_mgr/alldata.html',{
            'leraning_time': leraning_time.objects.all().order_by('-id'),
            })
    else:
        form = inputform()
    return render(request, 'new_learn_mgr/page1.html',{'form': form})

def page2(request):
    pie_data = leraning_time.objects.all().values('category').annotate(total=Sum('time'))
    pie_label = [x['category'] for x in pie_data]
    pie_data = [x['total'] for x in pie_data]

    zipped_list = zip(pie_label, pie_data)

    return render(request, 'new_learn_mgr/page2.html',{
        'zipped_list': zipped_list,
        'pie_data': pie_data,
    })

def page3(request):
    return render(request, 'new_learn_mgr/page3.html')

#'test'