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
from lib import User, BaseHandler, NGO
from time import sleep


class RegistrationHandler(BaseHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.render("registration.html")
		else:
			self.redirect("/")
	def post(self):
		userChoice = self.request.get("userChoice")
		if userChoice=="ngo":
			self.redirect("/signup/ngoRegistration")
		else:
			self.redirect("/signup/userRegistration")

	
class UserRegistrationPage(BaseHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			userid = user.user_id()
 			authenticationUser = User.query(User.userid == userid).fetch(1)
			if  not authenticationUser:
				self.render("userRegistration.html")
			else:
				self.redirect("/home")
		else:
			self.redirect("/signup")
	
	def post(self):
		user= users.get_current_user()
		name = self.request.get("name")	
		userid = user.user_id()
		gender = self.request.get("gender")
		userObject = User()
		userObject.userid=userid
		userObject.name = name
		userObject.gender = gender
		userObject.projects = []
		userObject.put()
		sleep(5)
		self.redirect("/home")

class NGORegistrationPage(BaseHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			userid = user.user_id()
 			authenticationUser = NGO.query(NGO.userid == userid).fetch(1)
			if  not authenticationUser:
				self.render("ngoRegistration.html")
			else:
				self.redirect("/home")
		else:
			self.redirect("/signup")
	
	def post(self):
		user= users.get_current_user()
		name = self.request.get("name")	
		userid = user.user_id()
		ngoObject = NGO()
		ngoObject.userid = userid
		ngoObject.name = name
		ngoObject.credibility = False
		ngoObject.description = self.request.get("description")
		ngoObject.eightygRegistrationNumber = self.request.get("eightygRegistrationNumber")
		ngoObject.email = user.email()
		ngoObject.put()
		sleep(5) #cheap trick but none the less it works!
		self.redirect("/home")	

				
app = webapp2.WSGIApplication([('/signup/userRegistration',UserRegistrationPage), ('/signup/ngoRegistration',NGORegistrationPage),('/signup/registration',RegistrationHandler)],debug=True)	

