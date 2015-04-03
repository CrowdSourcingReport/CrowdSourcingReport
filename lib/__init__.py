	#oggpnosn
#hkhr

#library for essential and redundant function(templating)

from random import randint
import math
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
        address=ndb.StringProperty(required = True)
        lat=ndb.StringProperty(required = True)
        lng=ndb.StringProperty(required = True)
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
	sectorOfOperation = ndb.PickleProperty(required = True, indexed = True)
	#logo = ndb.BlobProperty()
	address = ndb.StringProperty(required = True)
	telephone = ndb.PickleProperty(required = True)
	registrationNumber = ndb.StringProperty(required = True)	
	#proofOfRegistration = ndb.BlobKeyProperty()


#data model for storing project data 
class Project(ndb.Model):
	title = ndb.StringProperty()
	ngo = ndb.StringProperty()
	authenticity = ndb.BooleanProperty()	
	category = ndb.StringProperty()	
	description = ndb.TextProperty()
	tasks = ndb.PickleProperty()
	#rewards = ndb.PickleProperty()
	address = ndb.StringProperty()
	date = ndb.StringProperty()
	lat = ndb.StringProperty()
	lng = ndb.StringProperty()
	funding = ndb.PickleProperty()
	#sectorOfOperation = ndb.StringProperty()
	def distance(self, x, y):
		print self.lat, self.lng
		for a in self.lat:
			print a
		return math.sqrt((float(x)-float(self.lat))**2 + (float(y)-float(self.lng))**2)

#data model for NGO Gov database
class NGOGOV(ndb.Model):
	pass
	
#base handler that cointains all the required charteristic
class BaseHandler(webapp2.RequestHandler):
        def render(self, filename, parameter = {}):
                parameter["users"] = users
                user = users.get_current_user()
                parameter["user"] = user
                projects = Project.query().fetch()
                randProjects = []
                try:
                    for i in range(0,4):
                        randomInt = randint(0,len(projects)-1)
                        if projects[randomInt] not in randProjects:
                            randProjects.append(projects[randomInt])
                except:
                    pass
                parameter["projects"] = randProjects
                parameter["len"] = len(randProjects)
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
	
