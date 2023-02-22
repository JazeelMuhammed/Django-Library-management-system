from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from .forms import bookform, CreateMultiuserForm
from .models import Booklist


# Create your views here.

def homepage(request):
    return render(request,'home.html')

def uploadbook(request):
    form = bookform
    if request.method == "POST":
        form = bookform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return uploadview(request)
    return render(request, 'upload.html', {'form': form})

def uploadview(request):
    b=Booklist.objects.all()
    return render(request,'uploadview.html',{'books':b})

def delete_book(request,pk):
    d=Booklist.objects.get(pk=pk)
    d.delete()
    return uploadview(request)

def view_book(request,pk):
    v=Booklist.objects.get(pk=pk)
    return render(request,'book.html',{'instance':v})

def edit_book(request,pk):
    edit=Booklist.objects.get(pk=pk)
    form=bookform(instance=edit)
    if request.method=="POST":
        form=bookform(request.POST,request.FILES,instance=edit)
        if form.is_valid():
            form.save(commit=True)
            return uploadview(request)
        else:
            print("Invalid form")
    return render(request,'upload.html',{'form':form})


def adminhome(request):
    return render(request,'adminhome.html')

def teachersignup(request):
    form = CreateMultiuserForm
    if request.method=="POST":
        form = CreateMultiuserForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.is_manager=True
            f.save()
            return homepage(request)
    return render(request,'managersignup.html',{'form':form})

def studentsignup(request):
    form = CreateMultiuserForm
    if request.method=="POST":
        form = CreateMultiuserForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.is_labour=True
            f.save()
            return homepage(request)
    return render(request,'laboursignup.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user and user.is_superuser==True:
            login(request,user)
            return adminhome(request)
        elif user and user.is_manager==True:
            login(request,user)
            return options(request)
        elif user and user.is_labour==True:
            login(request,user)
            return options(request)
        else:
            return HttpResponse("Invalid login details.....")

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return homepage(request)

def options(request):
    return render(request,'options.html')