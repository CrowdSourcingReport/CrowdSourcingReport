#oggpnosn
#hkhr

import webapp2
from lib import BaseHandler, NGO
import random 

class CredibilityCheckHandler(BaseHandler):
	def get(self):
		parameter = {}
		ngoQuery = NGO.query(NGO.credibility == False)
		ngoList = ngoQuery.fetch(10)
		parameter["ngoList"] = ngoList			
		self.render("adminCredibilityCheck.html", parameter)
			
class CredibilityCheckNGOHandler(BaseHandler):
	def get(self, userid):
		parameter = {}
		ngoQuery = NGO.query(NGO.userid == userid)	
		ngo = ngoQuery.fetch(1)
		parameter["ngo"] = ngo
		self.render("adminCredibilityCheckNGOPage.html", parameter)
				

class CreateFakeAccount(BaseHandler):
	def get(self):
		for i in range(100):
			ngo = NGO()
			ngo.name = str(random.randrange(20,10000))		
			ngo.credibility = False
			ngo.eightygRegistrationNumber = str(random.randrange(1,10000))
			ngo.description = str(random.randrange(1,100000000000000000000))
			ngo.userid = str(random.randrange(1,1000000))
			ngo.put()
		self.response.write("Done!")
app = webapp2.WSGIApplication([('/admin/CredibilityCheck', CredibilityCheckHandler),('/admin/fake',CreateFakeAccount),('/admin/CredibilityCheck/([0-9]+)', CredibilityCheckNGOHandler)])
