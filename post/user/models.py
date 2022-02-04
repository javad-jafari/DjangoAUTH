from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from passlib.handlers.django import django_pbkdf2_sha256
from post.utils import db
import uuid



class User:
    
    def start_session(self,user,req):

        req.session["logged_in"] = True
        req.session["user"] = user
        
        return JsonResponse(user, status=200)

    def signup(self,req):

        # create user obj

        user = {
            "_id" : uuid.uuid4().hex,
            "email" : req.POST.get("email"),
            "password":req.POST.get("password")

        }

        # encrypt password
        user["password"] = make_password(user["password"])

        # check exist user

        if db.users.find_one({"email":user["email"]}):
            return JsonResponse({"error":"user is already exist !"}, status=400)
        
        if db.users.insert_one(user):
            return self.start_session(user,req)

    
        return JsonResponse({"error":"signup failed !"}, status=400)

    
    def signout(self):
        return redirect("/")
    

    def signin(self, req):

        email = req.POST["email"]
        password = req.POST["password"]
        
        user = db.users.find_one({"email":email})

        if user and django_pbkdf2_sha256.verify(password, user["password"] ):

            return self.start_session(user, req)
        return HttpResponse("bad request or not found user") 
