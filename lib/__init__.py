#oggpnosn
#hkhr

#library for essential and redundant function(templating)

import jinja2
import os
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users
from datetime import datetime 

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
	eightygRegistration = ndb.BlobKeyProperty()
	description = ndb.TextProperty(required = True)
	email = ndb.StringProperty(required = True)
	projects = ndb.PickleProperty()
	pancardProof = ndb.BlobKeyProperty()
	pancardNumber = ndb.StringProperty(required = True)
	dateOfRegistration = ndb.DateTimeProperty(required = True)
	stateOfRegistration = ndb.StringProperty(required = True)
	chiefFunctionary = ndb.StringProperty(required = True)
	chairman = ndb.StringProperty(required = True)
	stateOfOperation = ndb.PickleProperty(required = True)
	sectorOfOperation = ndb.PickleProperty(required = True)
	logo = ndb.BlobProperty()
	address = ndb.StringProperty(required = True)
	telephone = ndb.PickleProperty(required = True)
	registrationNumber = ndb.StringProperty(required = True)	
	proofOfRegistration = ndb.BlobKeyProperty()

#data model for storing the tasks
class TaskList(ndb.Model):
        taskTitle = ndb.StringProperty(required=True)
	taskDescription = ndb.TextProperty(required = True)
	taskFund = ndb.StringProperty(required=True)

#data model for storing project data 
class Project(ndb.Model):
	title = ndb.StringProperty()
	ngo = ndb.StringProperty()
	authenticity = ndb.BooleanProperty()	
	category = ndb.StringProperty()	
        Description = ndb.TextProperty()
        tasks = ndb.StructuredProperty(TaskList, repeated = True)

#data model for NGO Gov database
class NGOGOV(ndb.Model):
	pass
	
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
	def date(self,dateString):
		dateString = dateString.split("-")
		return datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]) )
	
