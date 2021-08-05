from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def access(request):
    user = User.objects.filter(username = request.POST(['username']))
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/login/')
    messages.error(request, 'That username is not in the system')
    return redirect('/register/')

def register(request):
    return render(request, 'register.html')

def signin(request):
    if request.method == 'GET':
        return redirect('/register/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    scale = Scale.objects.all()
    context = {
        'scales': scale,
    }
    return render(request, 'dashboard.html', context)

def updateProfile(request):
    pass

def category(request):
    pass

def createCategory(request):
    pass

def editCategory(request):
    pass

def updateCategory(request):
    pass

def addPost(request):
    pass

def createPost(request):
    pass

def editPost(request):
    pass

def updatePost(request):
    pass