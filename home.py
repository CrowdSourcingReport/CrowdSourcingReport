#oggpnosn
#hkhr

import webapp2
from lib import BaseHandler, NGO, Project, User
import random 
from google.appengine.api import mail
from google.appengine.api import users

class HomePageHandler(BaseHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			userid = user.user_id()
			userAuthentication =  User.query(User.userid == userid).fetch(1)
			ngoAuthentication = NGO.query(NGO.userid == userid).fetch(1)
			if userAuthentication:
				self.render("userHomePage.html")
			elif ngoAuthentication:
				self.render("ngoHomePage.html")
			else:
				self.redirect("/signup/registration")
		else:
			self.redirect("/")
	
class ProjectUpdateHandler(BaseHandler):
	def get(self):
		user = users.get_current_user()
                if user:
                        userid = user.user_id()
                        userAuthentication =  User.query(User.userid == userid).fetch(1)
                        if userAuthentication:
				parameter = {}
				for userObject in userAuthentication:
					projects = userObject.projects
                                self.render("projectUpdate.html")
                        else:
                                self.redirect("/")
                else:   
                        self.redirect("/signup")
	

		
                



app = webapp2.WSGIApplication([('/home', HomePageHandler),('/home/ProjectUpdate',ProjectUpdateHandler)])



