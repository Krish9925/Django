from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    
    context = {'success':False}
    if request.method == 'POST':
        title= request.POST.get['title'] 
        desc= request.POST.get['desc']
        print(title,desc)
        ins = Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context = {'success':True}
    return render(request,'index.html', context)
def tasks(request):
    return render(request,'tasks.html')