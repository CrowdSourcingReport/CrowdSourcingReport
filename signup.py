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

#initializing jinja2 template 	
env=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

#initializing regular expression checker for email,password and username
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE=re.compile(r"^.{3,20}$")
EMAIL_RE=re.compile(r"^[\S]+@[\S]+\.[\S]+$")

#implementing password confirmation check
def verify_this(password,verify):
	if password==verify:
		return True
	else:
		return False

#implementing check for validity of password
def valid_password(password):
	ret=PASS_RE.match(password)
	if ret==None:
		return False
	else:
		return True

#implementing check for validity of username
def valid_username(username):
	ret=USER_RE.match(username)
	if ret==None:
                return False
        else:
                return True

#implementing check for validity of email
def valid_email(email):
        ret= EMAIL_RE.match(email)
	if email=='':
		return True
	if ret==None:
                return False
        else:
                return True

#data model for storing user data
class User(ndb.Model):
	name=ndb.StringProperty(required=True)
	username=ndb.StringProperty(required=True)
	password=ndb.StringProperty(required=True)
	email=ndb.StringProperty(required=True)

#main handler for /signup page
class SignUp(webapp2.RequestHandler):
	def get(self):
		template=env.get_template("Content/signup.html")	
		self.response.write(template.render())
	def post(self):
		name=self.request.get("name")
		username=self.request.get("username")
		password=self.request.get("password")
		confirmPassword=self.request.get("confirmPassword")
		emailId=self.request.get("emailId")
		#boolean to store validity of email,password and username
		emailValidity=valid_email(emailId)
		passwordValidity=valid_password(password)
		usernameValidity=valid_username(username)
		self.redirect("https://www.google.co.in/search?q=Election+Results&oi=ddle&ct=india-counting-day-2014-6044861157343232-hp&hl=en")

application=webapp2.WSGIApplication([('/signup',SignUp)],debug=True)	

