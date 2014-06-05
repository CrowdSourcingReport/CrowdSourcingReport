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


#data model for storing user data
class User(ndb.Model):
	name=ndb.StringProperty(required=True)
	username=ndb.StringProperty(required=True)
	password=ndb.StringProperty(required=True)
	email=ndb.StringProperty(required=True)

class AuthenticationPage(lib.BaseHandler):
	def get(self):
		user = users.get_current_user()
		if not user:
			parameter={}	
			parameter["signinUrlGoogle"] = users.create_login_url()
			self.render("authenticationPage.html",parameter=parameter)
		else:
			self.redirect("/home")
		
	

app = webapp2.WSGIApplication([('/signup', AuthenticationPage)],debug=True)	

