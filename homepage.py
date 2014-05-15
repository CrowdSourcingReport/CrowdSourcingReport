#oggpnosn
#hkhr
import webapp2
import random
import jinja2
import os

env=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class MainPage(webapp2.RequestHandler):
	def get(self):
		template=env.get_template("Content/frontPage.html")	
		self.response.write(template.render())

application=webapp2.WSGIApplication([('/',MainPage)],debug=True)	
