#oggpnosn
#hkhr
#script to implement signup

#importing essential library-----------------
import webapp2
import random
import jinja2
import os
import cgi
import re
from google.appengine.ext import ndb
import lib 
from google.appengine.api import users
from lib import User, BaseHandler


class RegistrationHandler(BaseHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.render("registration.html")
		else:
			self.redirect("/")
	def post(self):
		userChoice = self.request.get("userChoice")
		self.response.write(userChoice)		
		if userChoice=="ngo":
			self.redirect("/signup/UserRegistration")
		else:
			self.redirect("/signup/NGORegistration")

	
class UserRegistrationHandler(BaseHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			userid = user.user_id()
 			authenticationUser = User.query(User.userid == userid).fetch(1)
			if  not authenticationUser:
				self.render("userRegistration.html")
			else:
				self.redirect("/")
		else:
			self.redirect("/")
	
	def post(self):
		user= users.get_current_user()
		name = self.request.get("name")	
		userid = user.user_id()
		gender = self.request.get("gender")
		userObject = User()
		userObject.userid=userid
		userObject.name = name
		userObject.gender = gender
		userObject.put()
		self.redirect("/home")

class NGORegistrationHandler(BaseHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			userid = user.user_id()
 			authenticationUser = User.query(User.userid == userid).fetch(1)
			if  not authenticationUser:
				self.render("userRegistration.html")
			else:
				self.redirect("/")
		else:
			self.redirect("/")
	
	def post(self):
		user= users.get_current_user()
		name = self.request.get("name")	
		userid = user.user_id()
		gender = self.request.get("gender")
		userObject = User()
		userObject.userid=userid
		userObject.name = name
		userObject.gender = gender
		userObject.put()
		self.redirect("/home")
			
app = webapp2.WSGIApplication([('/signup/UserRegistration',UserRegistrationHandler),('/signup/registration',RegistrationHandler),('/signup/NGORegistration',NGORegistrationHandler)],debug=True)	

