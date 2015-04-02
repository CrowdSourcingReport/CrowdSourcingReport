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
		
class SignupHandler(BaseHandler):
	def get(self):
		self.render("Signup.html")

class RedirectHandler(BaseHandler):
	def get(self):
		self.render("Redirect.html")
	def post(self):
		self.render("Redirect.html")

class SearchHandler(BaseHandler):
	def get(self):
		searchString = self.request.get("searchString")
		q = ndb.gql("SELECT * FROM NGO WHERE name > :1 AND name < :2", searchString, unicode(searchString) + u"\ufffd").fetch(20)
		try:
			parameter = {}
			parameter["results"] = q
			parameter["search"] = searchString
			parameter["len"] = len(q)
			self.render("search.html", parameter)
		except search.Error:
			logging.exception("Search Failed")

class ProjectPageHandler(BaseHandler):
    def get(self):
        self.render("projectPage.html")		

class ngoPageHandler(BaseHandler):
    def get(self, urlParameter):
        q = NGO.query(NGO.userid == urlParameter).fetch(1)
        if q:
			parameters = {}
			for p in q:
				parameters["ngo"] = p
			q = Project.query(Project.ngo == urlParameter).fetch(4)
			parameters["projects"] = q
			parameters["p_len"] = len(q)
			q = NGO.query(NGO.userid != urlParameter and NGO.sectorOfOperation == parameters["ngo"].sectorOfOperation).fetch(4)
			parameters["similarNGOs"] = q
			parameters["n_len"] = len(q)
			self.render('ngoPage.html',parameters)
		

app = webapp2.WSGIApplication([('/', MainPageHandler),('/features', FeatureHandler),('/about', AboutHandler),('/explore', ExploreHandler), ('/WhatWeDo', WhatWeDoHandler),('/PrivacyPolicy', PrivacyPolicyHandler),('/Faq', FaqHandler),('/TermsOfUse', TermsOfUseHandler),('/Media', MediaHandler),('/Customers', CustomersHandler), ('/login', LoginHandler), ('/search', SearchHandler), ('/project', ProjectPageHandler),('/Signup', SignupHandler),('/Redirect', RedirectHandler),('/ngo/([A-Za-z0-9]+)', ngoPageHandler)],debug=True)

