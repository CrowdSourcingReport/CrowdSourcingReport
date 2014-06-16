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
from lib import NGO, BaseHandler, User

class ProposePage(BaseHandler):
        def get(self):
                user=users.get_current_user()
		if user:
			userid = user.user_id()
 	    		userAuthenticationQuery = User.query(User.userid == userid).fetch(1)	 	    	      
                        NGOauthenticationQuery = NGO.query(NGO.userid == userid).fetch(1)	 	    	      
			if (not userAuthenticationQuery) and (not NGOauthenticationQuery) :
				self.redirect("/signup/registration")
			else:
                                self.render("propose.html")
		else:
                        self.redirect("/login")
                
        def post(self):
                category = self.request.get("name")
                self.redirect("/propose/project")

class ProjectDetailsPage(BaseHandler):
        def get(self):
                self.render("project.html")

        def post(self):
                title = self.request.get("title")
                user=users.get_current_user()
                if user:
                        userid = user.user_id()
                        authenticationUser = User.query(User.userid==userid).fetch(1)
                        authenticationNGO = NGO.query(NGO.userid==userid).fetch(1)
                        if authenticationNGO:
                                self.redirect("/home")
                        elif authenticationUser:
                                self.redirect("/home")
                        else:
                                self.redirect("/")
                else:
                        self.redirect("/login")
                
                
app = webapp2.WSGIApplication([('/propose', ProposePage), ('/propose/project', ProjectDetailsPage)],debug=True)
