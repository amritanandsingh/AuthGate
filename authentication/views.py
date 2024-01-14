from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
# Create your views here.

def home(request):
    return render(request , "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.post.get("fname")
        lname = request.post.get("lname")
        email = request.post.get("email")
        password = request.post.get("password")
        password2 = request.post.get("password2")
        
        myuser = User.objects.create_user(username,email , password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request , "Your account has been sucessfully created.")
        return redirect('signin')

    return render(request, "authentication/signup.html" )

def signin(request):
    return render(request, "authentication/signin.html" )

def signout(request):
    pass