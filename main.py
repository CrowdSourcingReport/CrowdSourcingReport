#oggpnosn
#hkhr
import webapp2
from google.appengine.ext.webapp import template
import random
import jinja2
import os

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'html')),extensions=['jinja2.ext.autoescape'], autoescape=True)

class BaseHandler(webapp2.RequestHandler):
	def render(self, filename, parameter = {}):
		template = env.get_template(filename )
		self.response.write(template.render(parameter))
	
class MainPageHandler(BaseHandler):
	def get(self):
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
            self.render('feature.html')        
       
application=webapp2.WSGIApplication([('/', MainPageHandler),('/feature',FeatureHandler),('/about',AboutHandler),('/explore',ExploreHandler),('/propose',ProposeHandler)],debug=True)
