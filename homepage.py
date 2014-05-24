#oggpnosn
#hkhr
import webapp2
import random
import jinja2
import os
from google.appengine.ext.webapp import template
#env=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)
class BaseHandler(webapp2.RequestHandler):
        def render_template(self, view_filename, params = None):
            if not params:
                   params = {}
            path = os.path.join(os.path.dirname(__file__), 'Content/html', view_filename)
            self.response.out.write(template.render(path, params))
    
class MainPage(BaseHandler):
	def get(self):
#		template=env.get_template("Content/html/frontPage.html")	
#		self.response.write(template.render())
                self.render_template('frontpage.html')        
        
application=webapp2.WSGIApplication([('/',MainPage)],debug=True)	
