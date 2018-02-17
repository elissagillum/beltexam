from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
	def validateUser(self, post_data):
		errors = []
		if len(post_data["name"]) < 3:
			errors.append("Name must be at least three characters")

		if len(post_data["username"]) < 3:
			errors.append("Username must be at least three characters")

		if len(post_data["email"]) < 3:
			errors.append("Email address must be at least three characters")			

		if len(post_data["password"]) == 0:
			errors.append("Password must be at least three characters")		

		if post_data['password'] != post_data['password_confirm']:
			errors.append("Passwords do not match")	

		if len(errors) == 0:
			return True,
		else:
			return False, errors

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	birthday = models.DateField(auto_now=False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

class Friend(models.Model):
	username = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, related_name="friends", null=True)
	#user_id = models.ForeignKey(User, related_name="friends",null=True)


class Admin(models.Model):
	user = models.ForeignKey(User, related_name="admins")
	friend = models.ForeignKey(Friend, related_name="admins_friends")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)