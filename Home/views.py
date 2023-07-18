from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse('this is the homepage')
   
    return render(request, 'home.html')

def Stores(request):
    # return HttpResponse('this is the stores page')
    return render(request, 'stores.html')

def More_info(request):
    return render(request, 'more info.html')

def Contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        return render(request, 'home.html')
        messages.success(request, "Form has been submitted!")
    # return HttpResponse('this is where you can contact us')
    return render(request, 'contact us.html')