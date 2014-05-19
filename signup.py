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

#standard string definition
emailAlertMessage="Kindly Enter a valid email!"	
passwordAlertMessage="Password can cointain a-z, A-Z, 0-9, _ and - only, and a length in between 6 and 20"
usernameAlertMessage="Username can cointain a-z, A-Z, 0-9, _ and - only, and a length in between 6 and 20"
confirmPasswordAlertMessage="Password Dint Match!"
usernameAvailibilityAlertMessage="Username wasnt available"
inputWarning="inputWarning"

#initializing regular expression checker for email,password and username
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{6,20}$")
PASS_RE=re.compile(r"^[a-zA-Z0-9_-]{6,20}$")
EMAIL_RE=re.compile(r"^[\S]+@[\S]+\.[\S]+$")


#implementing password confirmation check
def verify_password(password,verify):
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
	if ret==None:
                return False
        else:
                return True

#checking availibility of username
def username_availibility(username):
	#implementation left to Onuja :-}(a simple query!)
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
		template=env.get_template("Content/signup.html")	
		name=self.request.get("name")
		username=self.request.get("username")
		password=self.request.get("password")
		confirmPassword=self.request.get("confirmPassword")
		emailId=self.request.get("emailId")
		#boolean to store validity of email,password and username
		emailValidity=valid_email(emailId)
		passwordValidity=valid_password(password)
		usernameValidity=valid_username(username)
		confirmPasswordValidity=verify_password(password,confirmPassword)
		usernameAvailibility=username_availibility(username)
		#if all the validity condition are passed then move on to storing data 
		if emailValidity and passwordValidity and usernameValidity and confirmPasswordValidity and usernameAvailibility:
			user=User()
			user.name=name
			user.username=username
			user.password=password
			user.email=emailId
			user.put()
			self.response.write("success!")
		else:
		#otherwise generate appropriate error message to help user through registration process
			alertMessage={}
			if not emailValidity:
				alertMessage["emailAlertMessage"]=emailAlertMessage
			if not usernameValidity:
				alertMessage["usernameAlertMessage"]=usernameAlertMessage
			elif not usernameAvailibility:
				alertMessage["usernameAlertMessage"]=usernameAvailibilityAlertMessage
			if not passwordValidity:
				alertMessage["passwordAlertMessage"]=passwordAlertMessage
			if not confirmPasswordValidity:
				alertMessage["confirmPasswordAlertMessage"]=confirmPasswordAlertMessage
			alertMessage["inputWarningPassword"]=inputWarning	
			self.response.write(template.render(alertMessage))	

application=webapp2.WSGIApplication([('/signup',SignUp)],debug=True)	

