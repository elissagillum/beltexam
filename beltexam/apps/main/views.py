from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
	context = {
	'users': User.objects.all(),
	'friends': Friend.objects.all()
	}
	return render(request, "main/index.html", context)

def register(request):
	valid = User.objects.validateUser(request.POST)
	if valid[0]:
		pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
		User.objects.create(name=request.POST["name"], username=request.POST["username"], email=request.POST["email"], password=pw_hash, birthday=request.POST["birthday"])
		messages.success(request,"Finished registering, please log in")
	else:
		for error in valid[1]:
			messages.error(request, error)
	return 	redirect("/")

def login(request):
	try:
		user = User.objects.get(email = request.POST["email"])
		print user
		password = request.POST["password"]
		if bcrypt.checkpw(password.encode(), user.password.encode()):
			request.session["user_id"] = user.id
			return redirect("/friends")
		else:
			messages.error(request, "Password does not match")
			return redirect("/")
	except:
		messages.error(request, "Can't log on")
		return redirect("/")

def success(request):
	if request.method =="POST":
		friend = Friend.objects.get(id=user_id)
		friend.username = request.POST["username"]
		friend.name = request.POST["name"]
		friend.save()
		return redirect("/friends")
	else:
		context = {
		"user" : User.objects.get(id = request.session["user_id"]),
		"friends" : Friend.objects.get(id=request.session["user_id"])
		}
	return render(request, "main/friends.html", context)

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def users(request):
	context = {
	'friends': Friend.objects.all()
	}
	return render(request, "main/userprofile.html", context)

def delete(request):
	Friend.objects.get(id=friend_id).delete()
	return redirect (request, "/friends")