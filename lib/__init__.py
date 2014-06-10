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
        userid=ndb.StringProperty(required=True)
        name=ndb.StringProperty(required=True)
        gender=ndb.StringProperty(required=True)

#base handler that cointains all the required charteristic
class BaseHandler(webapp2.RequestHandler):
        def render(self, filename, parameter = {}):
                parameter["users"] = users
                user = users.get_current_user()
                parameter["user"] = user
                template = env.get_template(filename )
                self.response.write(template.render(parameter))


