from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')
    ##return HttpResponse("This IS Home Page")

def video(request):
    return render(request,'video.html')

def blog(request):
    return render(request,'blogs.html')

def portfolio(request):
    return render(request,'portfolio.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        contact = Contact(name=name,number=number,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')