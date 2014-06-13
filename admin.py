#oggpnosn
#hkhr

import webapp2
from lib import BaseHandler, NGO, Project
import random 
from google.appengine.api import mail

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
		parameter["ngoList"] = ngo
		self.render("adminCredibilityCheckNGOPage.html", parameter)
	def post(self, userid):
		descriptionAuthenticity = self.request.get("descriptionAuthenticity")			
		eightygAuthenticity = self.request.get("eightygAuthenticity")
		ngoQuery = NGO.query(NGO.userid == userid)
                ngoList = ngoQuery.fetch(1)

		if descriptionAuthenticity == "on" and eightygAuthenticity == "on":
			for ngo in ngoList:	
				mail.send_mail(sender=" <tanaygahlot@gmail.com>",
    					          to= "<"+ngo.email+">",
              					subject="Your NGO has been approved",
              					body="""Dear :"""+ngo.name+"""\nYour csr.com account has been approved.  You can now visit
http://www.csr.com/ and sign in using your Google Account to access new features.Please let us know if you have any questions.
The csr.com Team
""")				
		else:
			failiureReport = "\nPlaces where your ngo failed\n"
			if descriptionAuthenticity != "on":	
				failiureReport+=" The Description you provided isnt apt for a site like us.\n"
			elif eightygAuthenticity != "off": 
				failiureReport+=" Your 80G no isnt valid\n"
			for ngo in ngoList:
                                mail.send_mail(sender=" <tanaygahlot@gmail.com>",
                                                  to= "<"+ngo.email+">",
                                                subject="Your NGO has failed authentication test",
                                                body="""Dear :"""+ ngo.name + failiureReport +"""Please let us know if you have any questions.
The csr.com Team
""")
			
class CreateFakeNGOAccount(BaseHandler):
	def get(self):
		for i in range(100):
			ngo = NGO()
			ngo.name = str(random.randrange(20,10000))		
			ngo.credibility = False
			ngo.eightygRegistrationNumber = str(random.randrange(1,10000))
			ngo.description = str(random.randrange(1,100000000000000000000))
			ngo.userid = str(random.randrange(1,1000000))
			ngo.email = "tanaygahlot@gmail.com"
			ngo.put()
		self.response.write("Done!")

class CreateFakeProject(BaseHandler):
	def get(self):
		for i in range(100):
                        project = Project()
                        project.title = str(random.randrange(20,10000))
                        project.authenticity = False
                        project.description = str(random.randrange(1,100000000000000000000))
                        project.ngo = str(random.randrange(1,1000000))
                        project.put()
                self.response.write("Done!")
	
	

class AdminHandler(BaseHandler):
	def get(self):
		self.render("adminHomePage.html")

class AuthenticateHandler(BaseHandler):
        def get(self):
                parameter = {}
                projectQuery = Project.query(Project.authenticity == False)
                projectList = projectQuery.fetch(10)
                parameter["projectList"] = projectList
                self.render("adminAuthenticate.html", parameter)


class AuthenticateProjectHandler(BaseHandler):
        def get(self, userid):
                parameter = {}
                projectQuery = Project.query(Project.userid == userid)
                project = projectQuery.fetch(1)
                parameter["projectList"] = ngo
                self.render("adminCredibilityCheckNGOPage.html", parameter)
        def post(self, userid):
                descriptionAuthenticity = self.request.get("descriptionAuthenticity")
                eightygAuthenticity = self.request.get("eightygAuthenticity")
                ngoQuery = NGO.query(NGO.userid == userid)
                ngoList = ngoQuery.fetch(1)

                if descriptionAuthenticity == "on" and eightygAuthenticity == "on":
                        for ngo in ngoList:
                                mail.send_mail(sender=" <tanaygahlot@gmail.com>",
                                                  to= "<"+ngo.email+">",
                                                subject="Your NGO has been approved",
                                                body="""Dear :"""+ngo.name+"""\nYour csr.com account has been approved.  You can now visit
http://www.csr.com/ and sign in using your Google Account to access new features.Please let us know if you have any questions.
The csr.com Team
""")
                else:
                        failiureReport = "\nPlaces where your ngo failed\n"
                        if descriptionAuthenticity != "on":
                                failiureReport+=" The Description you provided isnt apt for a site like us.\n"
                        elif eightygAuthenticity != "off":
                                failiureReport+=" Your 80G no isnt valid\n"
                        for ngo in ngoList:
                                mail.send_mail(sender=" <tanaygahlot@gmail.com>",
                                                  to= "<"+ngo.email+">",
                                                subject="Your NGO has failed authentication test",
                                                body="""Dear :"""+ ngo.name + failiureReport +"""Please let us know if you have any questions.
The csr.com Team
""")

app = webapp2.WSGIApplication([('/admin/CredibilityCheck', CredibilityCheckHandler),('/admin/fake/NGO',CreateFakeNGOAccount),('/admin/fake/Project',CreateFakeProject),('/admin/CredibilityCheck/([0-9]+)', CredibilityCheckNGOHandler), ('/admin', AdminHandler ), ('/admin/Authenticate', AuthenticateHandler), ('/admin/Authenticate/([0-9]+)', AuthenticateProjectHandler)])
