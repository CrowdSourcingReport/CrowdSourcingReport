#oggpnosn
#hkhr
import webapp2
from google.appengine.ext.webapp import template
import random
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from lib import User,BaseHandler, NGO

class MainPageHandler(BaseHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			userid = user.user_id()
 	    		userAuthenticationQuery = User.query(User.userid == userid).fetch(1)	 	    	      
                        NGOauthenticationQuery = NGO.query(NGO.userid == userid).fetch(1)
                        if (not userAuthenticationQuery) and (not NGOauthenticationQuery) :
				self.redirect("/signup/registration")
			else:
                                self.redirect("/home")
		self.render('frontPage.html')        
   

class UserDashboardHandler(BaseHandler):
        def get(self):
                user=users.get_current_user()
		if user:
			userid = user.user_id()
 	    		userAuthenticationQuery = User.query(User.userid == userid).fetch(1)	 	    	      
                        if not userAuthenticationQuery:
				self.redirect("/signup/userRegistration")
			else:
                                self.render('userDashboard.html')
		else:
                        self.redirect("/signup")

class SignupHandler(BaseHandler):
        def get(self):
                self.render("login.html")
                
class NGODashboardHandler(BaseHandler):
        def get(self):
                user=users.get_current_user()
		if user:
			userid = user.user_id()
 	    		NGOAuthenticationQuery = NGO.query(NGO.userid == userid).fetch(1)	 	    	      
                        if not NGOAuthenticationQuery:
				self.redirect("/signup/ngoRegistration")
			else:
                                self.render('ngoDashboard.html')
		else:
                        self.redirect("/signup")

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



       

app = webapp2.WSGIApplication([('/', MainPageHandler),('/features', FeatureHandler),('/about', AboutHandler),('/explore', ExploreHandler),('/propose', ProposeHandler),('/home', HomeHandler),('/WhatWeDo', WhatWeDoHandler),('/PrivacyPolicy', PrivacyPolicyHandler),('/Faq', FaqHandler),('/TermsOfUse', TermsOfUseHandler),('/Media', MediaHandler),('/Customers', CustomersHandler)],debug=True)

