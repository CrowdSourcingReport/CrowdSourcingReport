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
from lib import NGO, BaseHandler, User, Project, TaskList
from time import sleep

class ProposePage(BaseHandler):
        def get(self):
                user=users.get_current_user()
		if user:
			userid = user.user_id()
                        NGOauthenticationQuery = NGO.query(NGO.userid == userid).fetch(1)	 	    	      
			if not NGOauthenticationQuery :
				self.redirect("/signup/registration")
			else:
                                self.render("propose.html")
		else:
                        self.redirect("/login")
                
        def post(self):
                category = self.request.get("category")
		title = self.request.get("title")
                user=users.get_current_user()
                userid = user.user_id()
                projectObject = Project()
                projectObject.ngo = userid
                projectObject.category = category
		projectObject.title = title 
		projectObject.authenticity = False
                projectObject.put()
		self.response.headers.add_header("Set-Cookie",str("title=%s"%title))
                sleep(5)
                self.redirect("/propose/project")

class ProjectDetailsPage(BaseHandler):
        def get(self):
		user = users.get_current_user()
		if user:
			title = self.request.cookies.get("title", None)
			userid = user.user_id()
			project = Project.query(Project.ngo == userid, Project.title == title).fetch(1)[0]
			if project:
				self.render("project.html")
			else:
				self.redirect("/propose")
			
		else:
			self.redirect("/login")

        def post(self):
                shortDescription = self.request.get("shortDescription")
		user = users.get_current_user()
		userid = user.user_id()
		title = self.request.cookies.get("title", "")
                project = Project.query(Project.ngo == userid, Project.title == title).fetch(1)[0]
		project.shortDescription = shortDescription             
		project.put()
		self.redirect("/propose/project/taskList")

class ProjectTaskPage(BaseHandler):
        def get(self):
                self.render("projectTaskPage.html")

        def post(self):
                detailedDescription = self.request.get("detailedDescription")
                
                count=int(self.request.get("count"))
                projectObject = Project()
                user=users.get_current_user()
                if user:
                        userid = user.user_id()
                        authenticationUser = User.query(User.userid==userid).fetch(1)
                        authenticationNGO = NGO.query(NGO.userid==userid).fetch(1)
                        if authenticationNGO:
                                ngo = projectObject.ngo
                                existingProject = Project.query(Project.ngo==userid).fetch(1)
                                if existingProject:
                                        projectObject.detailedDescription = detailedDescription
                                        while count>0:
                                                j=1
                                                Counter=str(count-count+j)
                                                taskTitle = self.request.get("taskTitle"+Counter)
                                                taskDescription = self.request.get("taskDescription"+Counter)
                                                taskFund = self.request.get("taskFund"+Counter)
                                                count=count-1
                                                j=j-1
                                                projectObject.tasks = [TaskList(taskTitle = taskTitle, taskDescription = taskDescription, taskFund = taskFund)]
                                        projectObject.put()
                                        self.redirect("/home")
                                else:
                                        self.redirect("/propose")
                        elif authenticationUser:
                                self.redirect("/home")
                        else:
                                self.redirect("/")
                else:
                        self.redirect("/login")
                        
                
app = webapp2.WSGIApplication([('/propose', ProposePage), ('/propose/project', ProjectDetailsPage), ('/propose/project/taskList', ProjectTaskPage)],debug=True)
