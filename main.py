#oggpnosn
#hkhr
from random import randint
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
		projects = Project.query().fetch()
		randProjects = []
		try:
			for i in range(0,4):
				randomInt = randint(0,len(projects)-1)
				if projects[randomInt] not in randProjects:
					randProjects.append(projects[randomInt])
		except:
			pass
		parameter = {"projects" : randProjects }
		self.render('frontPage.html', parameter)        
   

class SignupHandler(BaseHandler):
        def get(self):
                self.render("login.html")
                

class ExploreHandler(BaseHandler):
	def get(self):
		parameter = {}
		parameter["get"]=1
		self.render('explore.html',parameter)        

	def post(self):
		parameter = {}
		lat = self.request.get("lat")
		lng = self.request.get("lng")
		print lat, lng
		projects = Project.query().fetch()
		decorated = [(project,project.distance(lat,lng)) for project in projects if project.distance(lat,lng)<1.00]
		closeProjects = sorted(decorated, key=lambda tup: tup[1])
		parameter["closeProjects"] = closeProjects
		parameter["get"] = 0
		parameter["search"] = self.request.get("address")
		parameter["length"] = len(parameter["closeProjects"])
		self.render('explore.html',parameter)

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

class ProjectPageDemoHandler(BaseHandler):
    def get(self):
        self.render("projectPageDemo.html")		
        
class ProjectPageHandler(BaseHandler):
    def get(self,urlParameter):
		ngo, title = urlParameter.split("_")
		q = Project.query(Project.title == title and Project.ngo == ngo).fetch(1)
		funds = 0
		print q
		if q:
			parameters = {}
			for p in q:
				parameters["project"] = p
				ngoP = NGO.query(NGO.userid == p.ngo).fetch(1)
				parameters["ngo"] = ngoP[0]
			for task in parameters["project"].tasks:
				funds = funds + int(task[2]);
			i=0
			parameters["collected"] = 0
			parameters["funding"] = []
			while i < len(parameters["project"].funding):
				user = User.query(User.userid == parameters["project"].funding[i][0]).fetch(1)
				parameters["collected"] = parameters["collected"] + int(parameters["project"].funding[i][1])
				parameters["funding"].append((user[0], parameters["project"].funding[i][1]))
				i=i+1
			print parameters["project"].funding
			parameters["support"]=i
			print parameters["support"]
			projects = Project.query(Project.category == parameters["project"].category).fetch()
			closeProjects = []
			try:
				for i in range(0,4):
					randomInt = randint(0,len(projects)-1)
					if(projects[randomInt] not in closeProjects and projects[randomInt] != parameters["project"]):
						closeProjects.append(projects[randomInt])
			except:
				pass
			parameters["closeProjects"] = closeProjects
			parameters["funds"] = funds
			self.render("projectPage.html", parameters)

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

class FundHandler(BaseHandler):
	def get(self, urlParameter):
		ngo, title = urlParameter.split("_")
		q = Project.query(Project.title == title and Project.ngo == ngo).fetch(1)
		if q:
			parameters = {}
			for p in q:
				ngoP = NGO.query(NGO.userid == p.ngo).fetch(1)
				parameters["ngo"] = ngoP[0]
				parameters["project"] = p
			self.render('fund.html',parameters)

	def post(self,urlParameter):
		flag = 0;
		link = self.request.get("project")
		user=users.get_current_user()
		if user:
			userid = user.user_id()
			userAuth = User.query(User.userid == userid).fetch(1)
			if userAuth:
				funds = self.request.get("funds")
				ngo, title = link.split("_")
				q = Project.query(Project.title == title and Project.ngo == ngo).fetch(1)
				for p in userAuth[0].projects:
					if p[0] == link:
						p[1] = p[1] + funds
						flag = 1
				if(flag == 0):
					userAuth[0].projects.append([link,funds])
				userAuth[0].put()
				q[0].funding.append((userid,funds))
				q[0].put()
				parameter = {"message":"You Have Successfully Funded a Project."}
			else:
				parameter = {"message":"You Are Not Authorized to Fund a Project."}
		else:
			parameter = {"message":"Please Login to Fund a Project."}
		self.render("message.html",parameter)
		

app = webapp2.WSGIApplication([('/', MainPageHandler),('/features', FeatureHandler),('/about', AboutHandler),('/explore', ExploreHandler), ('/WhatWeDo', WhatWeDoHandler),('/PrivacyPolicy', PrivacyPolicyHandler),('/Faq', FaqHandler),('/TermsOfUse', TermsOfUseHandler),('/Media', MediaHandler),('/Customers', CustomersHandler), ('/login', LoginHandler), ('/search', SearchHandler), ('/project', ProjectPageDemoHandler),('/Signup', SignupHandler),('/Redirect', RedirectHandler),('/ngo/([A-Za-z0-9]+)', ngoPageHandler),('/project/([A-Za-z0-9_]+)', ProjectPageHandler),("/fund/([A-Za-z0-9_]+)",FundHandler)],debug=True)

