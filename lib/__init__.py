#oggpnosn
#hkhr

#library for essential and redundant function(templating)

import jinja2
import os
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'..','html')), extensions=['jinja2.ext.autoescape'], autoescape=True)

#data model for storing user data
class User(ndb.Model):
        userid=ndb.StringProperty(required = True)
        name=ndb.StringProperty(required = True)
        gender=ndb.StringProperty(required = True)
	projects =  ndb.PickleProperty(required = True)

#data model for storing ngo data 
class NGO(ndb.Model):
	userid = ndb.StringProperty(required = True)
	name = ndb.StringProperty(required = True)
	credibility = ndb.BooleanProperty(required = True)
	eightygRegistrationNumber = ndb.StringProperty()
	description = ndb.TextProperty(required = True)
	email = ndb.StringProperty(required = True)
	projects = ndb.PickleProperty()
	proofOfRegistration = ndb.BlobProperty()
	panCardNumber = ndb.StringProperty()

#data model for storing the tasks
class TaskList(ndb.Model):
        taskTitle = ndb.StringProperty(required=True)
	taskDescription = ndb.TextProperty(required = True)
	taskFund = ndb.StringProperty(required=True)

#data model for storing project data 
class Project(ndb.Model):
	title = ndb.StringProperty()
	shortDescription = ndb.TextProperty()
	ngo = ndb.StringProperty()
	authenticity = ndb.BooleanProperty()	
	category = ndb.StringProperty()	
        detailedDescription = ndb.TextProperty()
        tasks = ndb.StructuredProperty(TaskList, repeated = True)
	
	
#base handler that cointains all the required charteristic
class BaseHandler(webapp2.RequestHandler):
        def render(self, filename, parameter = {}):
                parameter["users"] = users
                user = users.get_current_user()
                parameter["user"] = user
                template = env.get_template(filename )
                self.response.write(template.render(parameter))
	def uniqueIdentifierProject(self, project):
		return project.ngo+"_"+project.title

	def stripProjectIdentifier(self, identifier):
		split = identifier.split("_") 
		return (split[0], split[1])

