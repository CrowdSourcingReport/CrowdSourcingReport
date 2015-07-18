#oggpnosn
#hkhr

import webapp2
from lib import BaseHandler, NGO, Project, User
import random 
from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import ndb
#yo i m chenna
class HomePageHandler(BaseHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			userid = user.user_id()
			userAuthentication =  User.query(User.userid == userid).fetch(1)
			ngoAuthentication = NGO.query(NGO.userid == userid).fetch(1)
			if userAuthentication:
				parameter = {}
				ngos = NGO.query().fetch(4)
				userObject = userAuthentication[0]
				userProjects = []
				for p in userObject.projects:
					ngo, title = p[0].split("_")
					print p[0]
					proj = ndb.gql("SELECT * FROM Project WHERE link = :1 AND ngo = :2", title,ngo).fetch(1)
					if proj:
						userProjects.append(proj[0]);
				projects = Project.query().fetch(100)
				print userObject.projects
				cProjects = []
				decorated = [(project,project.distance(userAuthentication[0].lat,userAuthentication[0].lng)) for project in projects if project.distance(userAuthentication[0].lat,userAuthentication[0].lng)<50]
				print decorated
				cProjects = sorted(decorated, key=lambda tup: tup[1])[0:4] 
				parameter["cProjects"] = cProjects
				parameter["userProjects"] = userProjects 
				parameter["ngos"] = ngos
				parameter["currUser"] = userAuthentication[0]
				self.render("userHomePage.html", parameter)
			elif ngoAuthentication:
				parameter={}
				proj = Project.query(Project.ngo == ngoAuthentication[0].userid).fetch()
                                parameter["ngoProjects"] = proj
                                parameter["length"] = len(proj)
                                parameter["ngo"]=ngoAuthentication[0]
				self.render("ngoHomePage.html", parameter)
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
				userObject = userAuthentication[0]
				projectsIdentifier = userObject.projects[:10]
				projects = []
				for projectIdentifier in projectsIdentifier:
					key = ndb.Key("Project", projectIdentifier)
					projects.append(key.get())
				parameter["projects"] = projects
                                self.render("projectUpdate.html", parameter)
                        else:
                                self.redirect("/")
                else:   
                        self.redirect("/login")
	
class UpdateProjectHandler(BaseHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			userid = user.user_id()
			userAuthentication = NGO.query(NGO.userid == userid).fetch(1)
			if userAuthentication:
				parameter={}
				ngo = userAuthentication[0]
				projectsIdentifierList = ngo.projects
				projects = []
				for projectIdentifier in projectsIdentifierList:
					ngo, title = self.stripProjectIdentifier(projectIdentifier)
					projectObject = Project.query(Project.ngo == ngo, Project.title == title).fetch(1)[0]
					projects.append(projectObject)
				parameter["projects"] = projects
				self.render("updateProject.html", parameter)
			else:
				self.redirect("/")	
		else:
			self.redirect("/login")
		
                
app = webapp2.WSGIApplication([('/home', HomePageHandler),('/home/ProjectUpdate',ProjectUpdateHandler),('/home/UpdateProject', UpdateProjectHandler)])



