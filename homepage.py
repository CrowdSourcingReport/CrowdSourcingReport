#oggpnosn
#hkhr
import webapp2
from google.appengine.ext.webapp import template
import random
import jinja2
import os

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'html')),extensions=['jinja2.ext.autoescape'], autoescape=True)

class BaseHandler(webapp2.RequestHandler):
#	def render(self, filename, parameter = {}):
		#template = env.get_template(filename )
		#self.response.write(template.render(parameter))
#		path = os.path.join(os.path.dirname(__file__), 'html', filename)
#		self.response.out.write(template.render(path, parameter))

	def render(self, view_filename, params=None):
	    if not params:
		params = {}
	    #user = self.user_info
	    #params['user'] = user
	    path = os.path.join(os.path.dirname(__file__), 'html', 'frontPaqge.html')
	    self.response.out.write(template.render(path, params))
	
class MainPage(BaseHandler):
	def get(self):
            self.render('frontPage.html')        
        
application=webapp2.WSGIApplication([('/',MainPage)],debug=True)
