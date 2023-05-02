from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
import re
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    form = CustomerForm()
    submitted = False
    if request.method=='POST':

        print(request.POST)
        phone = request.POST.get('phone')
        res = re.match(r"^1[35678]\d{9}$", phone)

        if res != None:
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                submitted=True
                print('saved!')
                return render(request,'index.html',{'form':form,'submitted':submitted})

    return render(request,'index.html',{'form':form})

def about(request):
    return render(request,'about.html')
def company(request):
    return render(request,'company.html')
def contact(request):
    return render(request,'contact.html')
def price(request):
    return render(request,'price.html')

