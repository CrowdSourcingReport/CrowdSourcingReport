#oggpnosn
#hkhr

#library for essential and redundant function(templating)

import jinja2
import os
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'html')), extensions=['jinja2.ext.autoescape'], autoescape=True)

#base handler that cointains all the required charteristic
class BaseHandler(webapp2.RequestHandler):
	def render(self,filename, parameter={}):
		template = JINJA_ENVIRONMENT.get_template(filename)
	        self.response.write(template.render(parameter))
	
