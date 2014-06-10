#oggpnosn
#hkhr
import webapp2
from google.appengine.ext.webapp import template
import random
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'html')),extensions=['jinja2.ext.autoescape'], autoescape=True)

#data model for storing user data
class User(ndb.Model):
	userid=ndb.StringProperty(required=True)
	name=ndb.StringProperty(required=True)
	gender=ndb.StringProperty(required=True)

class BaseHandler(webapp2.RequestHandler):
	def render(self, filename, parameter = {}):
		template = env.get_template(filename )
		self.response.write(template.render(parameter))
	
class MainPageHandler(BaseHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			userid = user.user_id()
 	    		authenticationQuery = User.query(User.userid == userid).fetch(1)	 	    	      
			if not authenticationQuery:
				self.redirect("/signup/registration")    
		self.render('frontPage.html')        

class ProposeHandler(BaseHandler):
	def get(self):
            self.render('propose.html')        

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
		self.render('home.html')

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



       
application=webapp2.WSGIApplication([('/', MainPageHandler),('/features', FeatureHandler),('/about', AboutHandler),('/explore', ExploreHandler),('/propose', ProposeHandler),('/home', HomeHandler),('/WhatWeDo', WhatWeDoHandler),('/PrivacyPolicy', PrivacyPolicyHandler),('/Faq', FaqHandler),('/TermsOfUse', TermsOfUseHandler),('/Media', MediaHandler),('/Customers', CustomersHandler)],debug=True)
