from collections import UserList
from email import message
from itertools import product
from urllib.request import Request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from Papi.models import Product
from users.forms import User

# from forms import User


def index(request):
    return render(request, 'users/index.html')

# Create your views here.
def home(request):
    all_product = Product.objects.all()
    return render(request, 'users/home.html', {'product': all_product})

def register(request):
    if request.method =="POST":
       form =UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Hi {username}, your account was created successfully')
           return redirect('home')
    else:
        form = UserRegisterForm()       
    return render(request, 'users/register.html', {'form':form})    

@login_required
def profile(request):
   
    return render(request, 'users/profile.html')

@login_required
def admin(request):
    all_p = Product.objects.all()
     # all_users= User.objects.all() , 
    return render(request, 'users/admin.html', {'product':all_p})
    
# def admin(request):
#     # all_p = Product.objects.all()
#      all_users= User.objects.all() , 
#      return render(request, 'users/admin.html', {'User':all_users})
    

@login_required
def feedback(request):
    return render(request, 'users/EAC_Tourist_Feedback_Form.html')   

@login_required
def aboutuslab(request):
    return render(request, 'users/aboutulab.html')

@login_required
def usersTble(request):
    all_u = User.objects.all()
    return render(request, 'users/users.html', {'users1': all_u} ) 

@login_required
def productTble(request):
    all_u = Product.objects.all()
    return render(request, 'users/product.html', {'product': all_u} )     

def basedash(request):
    return render(request, 'users/basedash.html')   

def dash(request):
    return render(request, 'users/dashboard.html')     

def request(request):
    return render(request, 'users/requests.html')  

def stock(request):
    return render(request, 'users/stock.html')  

@login_required
def userdelete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return render(request, 'users/product.html')    


@login_required
def prodelete(request, id):
    pro = Product.objects.get(id=id)
    pro.delete()
    return render(request, 'users/product.html')    


# @login_required
# def userupdate(request, id):
#     user = User.objects.get(id=id)
#     user.name = document.getElementById("name")
#     user.email =document.getElementById("department")
#     user.phone = document.getElementById("phone")
#     user.save()
#     return render(request, '')         

          
