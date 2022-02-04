from django.http import HttpResponse
from django.shortcuts import redirect, render
from post.user.models import User
from post.decorators import login_requierd





@login_requierd
def index(request):

    return HttpResponse(f"welcome {request.user}/{request.session['user']} ")


def signup(request):
    if request.method == "POST":
       user = User().signup(request)
       if user:
           return redirect("/")
        
    return render(request,'signup.html')


def signin(request):

    if request.method == "POST":
    
        return User().signin(request)
    return render(request, "signin.html")


def signout(request):
    respons= User().signout(request)
    respons.delete_cookie("sessionid")
    return respons