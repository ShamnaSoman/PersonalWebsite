from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Note, User


# Create your views here.
def home(request):
    return render(request, 'Home.html')


def about(request):
    return render(request , 'About.html')


def contact(request):
    return render(request , 'contact.html')


def gallery(request):
    return render(request ,'Gallery.html')


def note(request):
    if request.method == 'POST':
        print('Hello')
        print(request.POST.get('nameF'))
        print(request.POST.get('emailF'))
        print(request.POST.get('noteF'))
        if request.POST.get('nameF') and request.POST.get('emailF') and request.POST.get('noteF'):
            print( request.POST.get('nameF'))
            post = Note()
            post.Name = request.POST.get('nameF')
            post.Email = request.POST.get('emailF')
            post.Message = request.POST.get('noteF')
            post.save()

        return redirect('home')
    else:
        return render(request , 'Note.html')


def signup(request):
    print('start')
    if request.method == 'POST':
        print('123')
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('password'):
            if User.objects.filter(Email=request.POST.get('email')):
                messages.info(request, 'User already exist for this Email')
                return render(request,'Signup.html')
            else:
                post = User()
                post.Name = request.POST.get('name')
                post.Email = request.POST.get('email')
                post.Password = request.POST.get('password')
                print('write')
                post.save()
                print('saved')

        return redirect('signin')
    else:
        return render(request, 'Signup.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)

        if User.objects.filter(Email=email, Password=password).exists():
            print('exist')
            return redirect('home')
        else:
            messages.info(request,'The Email and Password does not match')
            return render(request,'Signin.html')
    else:
        return render(request, 'Signin.html')


def show(request):
    users = User.objects.all()
    return render(request,'Show.html',{'users':users})