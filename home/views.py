from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact,blog
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        title=request.POST.get('title')
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        time=datetime.now().strftime("%d/%m/%Y(%H:%M:%S)")

        contacts=Contact(message_title=title,name=name,phone=phone,email=email,desc=desc,date=time)
        contacts.save()


    return render(request,"contact.html")

def blogpage(request):
    articles=blog.objects.all().order_by('-id')
    length=len(articles)
    context={'articles':articles,'length':length}
    print(context)
    return render(request,'blogpage.html',context)

def blogcontent(request,slug):
    article=blog.objects.all().filter(Slug=slug).first()
    context={'article':article}
    return render(request,'blogcontent.html',context)