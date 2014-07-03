#oggpnosn
#hkhr
import webapp2
from google.appengine.ext.webapp import template
import random
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from lib import User,BaseHandler, NGO, Project
from google.appengine.api import search
class MainPageHandler(BaseHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			userid = user.user_id()
 	    		userAuthenticationQuery = User.query(User.userid == userid).fetch(1)	 	    	      
                        NGOauthenticationQuery = NGO.query(NGO.userid == userid).fetch(1)
                        if (not userAuthenticationQuery) and (not NGOauthenticationQuery) :
				self.redirect("/signup/registration")
		projects = Project.query().fetch(3)
		parameter = {"projects" : projects }
		self.render('frontPage.html', parameter)        
   

class SignupHandler(BaseHandler):
        def get(self):
                self.render("login.html")
                

class ExploreHandler(BaseHandler):
	def get(self):
                self.render('explore.html')        

class AboutHandler(BaseHandler):
	def get(self):
                self.render('aboutUs.html')        

class FeatureHandler(BaseHandler):
	def get(self):
                self.render('features.html')        

class HomeHandler(BaseHandler):
	def get(self):
		self.render('frontPage.html')

class WhatWeDoHandler(BaseHandler):
	def get(self):
                self.render('WhatWeDo.html')        

class CustomersHandler(BaseHandler):
	def get(self):
                self.render('Customers.html')
                
class MediaHandler(BaseHandler):
	def get(self):
                self.render('Media.html')        

class TermsOfUseHandler(BaseHandler):
	def get(self):
                self.render('TermsOfUse.html')        

class FaqHandler(BaseHandler):
	def get(self):
                self.render('Faq.html')        

class PrivacyPolicyHandler(BaseHandler):
	def get(self):
                self.render('PrivacyPolicy.html')        

class LoginHandler(BaseHandler):
	def get(self):
		self.render("login.html")

class SearchHandler(BaseHandler):
	def post(self):
		searchString = self.request.get("searchString")     
		index = search.Index(name = "NGO")		
		try:
			results = index.search(searchString)
			parameter = {}
			parameter["results"] = results
			self.render("search.html", parameter)
		except search.Error:
			logging.exception("Search Failed")
		

app = webapp2.WSGIApplication([('/', MainPageHandler),('/features', FeatureHandler),('/about', AboutHandler),('/explore', ExploreHandler), ('/WhatWeDo', WhatWeDoHandler),('/PrivacyPolicy', PrivacyPolicyHandler),('/Faq', FaqHandler),('/TermsOfUse', TermsOfUseHandler),('/Media', MediaHandler),('/Customers', CustomersHandler), ('/login', LoginHandler), ('/search', SearchHandler)],debug=True)

