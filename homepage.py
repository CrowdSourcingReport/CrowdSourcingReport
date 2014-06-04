#oggpnosn
#hkhr
import webapp2
import random
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'html')),extensions=['jinja2.ext.autoescape'], autoescape=True)
class BaseHandler(webapp2.RequestHandler):
	def render_template(self, filename, params = None):
		if not params:
			params = {}
		template = JINJA_ENVIRONMENT.get_template(filename )
		self.response.write(template.render()) 
class MainPage(BaseHandler):
	def get(self):
            self.render_template('frontPage.html')        
        
application=webapp2.WSGIApplication([('/',MainPage)],debug=True)	
