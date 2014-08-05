#oggpnosn
#hkhr
#changes are being made here by kethzi and priyanka

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
                ngo = ngoQuery.fetch(1)[0]
		parameter = {}
		if descriptionAuthenticity == "on" and eightygAuthenticity == "on":
			mail.send_mail(sender=" <tanaygahlot@gmail.com>",
    					          to= "<"+ngo.email+">",
              					subject="Your NGO has been approved",
              					body="""Dear :"""+ngo.name+"""\nYour csr.com account has been approved.  You can now visit http://www.csr.com/ and sign in using your Google Account to access new features.Please let us know if you have any questions.The csr.com Team		""")			
			ngo.credibility = True
			ngo.put()	
			parameter["message"]= "Success Mail Sent!"
			self.render("responseAdmin.html", parameter)

		else:
			failiureReport = "\nPlaces where your ngo failed\n"
			if descriptionAuthenticity != "on":	
				failiureReport+=" The Description you provided isnt apt for a site like us.\n"
			elif eightygAuthenticity != "off": 
				failiureReport+=" Your 80G no isnt valid\n"
			mail.send_mail(sender=" <tanaygahlot@gmail.com>",
                                                  to= "<"+ngo.email+">",
                                                subject="Your NGO has failed authentication test",
                                                body="""Dear :"""+ ngo.name + failiureReport +"""Please let us know if you have any questions.The csr.com Team""")
			parameter["message"] = "Failure Report Sent!"
			self.render("responseAdmin.html", parameter)


class CreateFakeNGOAccount(BaseHandler):
	def get(self):
		for i in range(100):
			ngo = NGO()
			ngo.name = str(random.randrange(20,10000))		
			ngo.credibility = False
			ngo.eightygRegistrationNumber = str(random.randrange(1,10000))
			ngo.description = str(random.randrange(1,100000000000000000000))
			ngo.userid = str(random.randrange(1,10))
			ngo.email = "tanaygahlot@gmail.com"
			ngo.projects=[]
			ngo.put()
		self.response.write("Done!")

class CreateFakeProject(BaseHandler):
	def get(self):
		for i in range(100):
               	        project = Project()
                	project.title = str(random.randrange(20,10000))
                       	project.authenticity = False
                	project.description = str(random.randrange(1,100000000000000000000))
                        project.ngo = str(random.randrange(1,10))
			project.category = "Health"
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
        def get(self, urlParameter):
		ngo, title = urlParameter.split("_")
                parameter = {}
                projectQuery = Project.query(Project.ngo == ngo, Project.title == title)
                project = projectQuery.fetch(1)[0]
                parameter["project"] = project
                self.render("adminAuthenticateProjectPage.html", parameter)
        def post(self, urlParameter):
		ngoUserid, title = urlParameter.split("_")
                descriptionAuthenticity = self.request.get("descriptionAuthenticity")
                projectQuery = Project.query(Project.ngo == ngoUserid, Project.title == title)
		ngoQuery = NGO.query(NGO.userid == ngoUserid)
		ngo = ngoQuery.fetch(1)[0]
                project = projectQuery.fetch(1)[0]
		parameter = {}
                if descriptionAuthenticity == "on":
                        mail.send_mail(sender=" <tanaygahlot@gmail.com>",
                                       	          to= "<"+ngo.email+">",
	                                         	subject="Your Project  has passed authentication test",
	                                                body="""Dear :"""+ ngo.name + "Your Project titled '"+project.title+"' has passed authentication and goes live!\n" +"""Please let us know if you have any questions.The csr.com Team""")
			project.authenticity = True
			project.put()
			parameter["message"]= "Success Mail Sent!"
   		        self.render("responseAdmin.html", parameter)


                else:
                	failiureReport = "\nPlaces where your project failed\n"
                        failiureReport += " The Description you provided isnt apt for a site like us.\n"
                        mail.send_mail(sender=" <tanaygahlot@gmail.com>", to= "<"+ngo.email+">", subject="Your Project has failed authentication test",body="""Dear :"""+ ngo.name + failiureReport +"""Please let us know if you have any questions. \nThe csr.com Team""")

			parameter["message"]= "Failure Report Sent!"
        	        self.render("responseAdmin.html", parameter)

app = webapp2.WSGIApplication([('/admin/CredibilityCheck', CredibilityCheckHandler),('/admin/fake/NGO',CreateFakeNGOAccount),('/admin/fake/Project',CreateFakeProject),('/admin/CredibilityCheck/([0-9]+)', CredibilityCheckNGOHandler), ('/admin', AdminHandler ), ('/admin/Authenticate', AuthenticateHandler), ('/admin/Authenticate/([0-9_a-zA-Z]+)', AuthenticateProjectHandler)])
