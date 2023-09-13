from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login_page/')
def receipes(request):
    if request.method == 'POST':
        data = request.POST
        img = request.FILES.get('receipe_img')
        
        name = data.get('receipe_name')
        desc = data.get('receipe_desc')
        Receipe.objects.create(receipe_name = name, receipe_desc = desc, receipe_img= img)
        return redirect('/receipe/')
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

@login_required(login_url='/login_page/')
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')


@login_required(login_url='/login_page/')
def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        img = request.FILES.get('receipe_img')
        name = data.get('receipe_name')
        desc = data.get('receipe_desc')
        # Receipe.objects.create(receipe_name = name, receipe_desc = desc, receipe_img= img)
        queryset.receipe_name = name
        queryset.receipe_desc = desc
        if img:
            queryset.receipe_img = img
        queryset.save()
        return redirect('/receipe/')


    context = {"receipe":queryset}
    return render(request, 'update_receipe.html', context)

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, 'user does not exist')
            return redirect('/login_page/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "username and password did not matched")
            return redirect('/login_page/')
        else:
            login(request, user)
            return redirect('/receipe/')
    return render(request, 'login.html')

        
def logout_page(request):
    logout(request)
    messages.info(request, 'logged out successfully!!')
    return  redirect('/login_page/')



def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'username already exist')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name= last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'account created successfully')
        return redirect('/register/')
    return render(request, 'register.html')
