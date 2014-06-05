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

#jinja templating environment
env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'html')), extensions=['jinja2.ext.autoescape'], autoescape=True)


#base handler that cointains all the required charteristic
class BaseHandler(webapp2.RequestHandler):
        def render(self,filename, parameter={}):
                template = env.get_template(filename)
                self.response.write(template.render(parameter))


#data model for storing user data
class User(ndb.Model):
	name=ndb.StringProperty(required=True)
	username=ndb.StringProperty(required=True)
	password=ndb.StringProperty(required=True)
	email=ndb.StringProperty(required=True)

class AuthenticationPage(BaseHandler):
	def get(self):
		user = users.get_current_user()
		if not user:
			parameter={}	
			parameter["signinUrlGoogle"] = users.create_login_url()
			self.render("authenticationPage.html", parameter)
		else:
			self.redirect("/home")
		
	

app = webapp2.WSGIApplication([('/signup', AuthenticationPage)],debug=True)	

