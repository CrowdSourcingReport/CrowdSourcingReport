#oggpnosn
#hkhr
import webapp2
import random
import jinja2
import os

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'html')),extensions=['jinja2.ext.autoescape'], autoescape=True)

class BaseHandler(webapp2.RequestHandler):
	def render(self, filename, parameter = {}):
		template = env.get_template(filename )
		self.response.write(template.render(parameter)) 

class MainPage(BaseHandler):
	def get(self):
            self.render('frontPage.html')        
        
application=webapp2.WSGIApplication([('/',MainPage)],debug=True)	
