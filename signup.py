#oggpnosn
#hkhr
#script to implement signup

#importing essential library-----------------
import webapp2
import random
import jinja2
import os
import cgi
import re
from google.appengine.ext import ndb
import lib 
from google.appengine.api import users
from lib import User, BaseHandler, NGO
from time import sleep
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import search

class RegistrationHandler(BaseHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.render("registration.html")
		else:
			self.redirect("/")
	def post(self):
		userChoice = self.request.get("userChoice")
		if userChoice=="ngo":
			self.redirect("/signup/ngoRegistration")
		else:
			self.redirect("/signup/userRegistration")

	
class UserRegistrationPage(BaseHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			userid = user.user_id()
 			authenticationUser = User.query(User.userid == userid).fetch(1)
			if  not authenticationUser:
				self.render("userRegistration.html")
			else:
				self.redirect("/home")
		else:
			self.redirect("/signup")
	
	def post(self):
		user= users.get_current_user()
		name = self.request.get("name")	
		userid = user.user_id()
		gender = self.request.get("gender")
		userObject = User()
		userObject.userid=userid
		userObject.name = name
		userObject.gender = gender
		userObject.projects = []
		userObject.put()
		sleep(5)
		self.redirect("/home")

class NGORegistration(BaseHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			userid = user.user_id()
 			authenticationUser = NGO.query(NGO.userid == userid).fetch(1)
			if  not authenticationUser:
				
				self.render("ngoRegistration.html")
			else:
				self.redirect("/home")
		else:
			self.redirect("/login")
	
	def post(self):
		user= users.get_current_user()
		if user:
			userid = user.user_id()
			authenticationUser = User.query(User.userid == userid).fetch(1)
			authenticationNgo = NGO.query(NGO.userid == userid).fetch(1)
			if authenticationUser or authenticationNgo:
				self.redirect("/home")
			else:
				name = self.request.get("name")	
				email = user.email()
				description = self.request.get("description")
				pancardNumber = self.request.get("pancardNumber")
				chiefFunctionary = self.request.get("chiefFunctionary")
				chairman = self.request.get("chairman")
				sectorOfOperation = self.request.get("sectorOfOperation")
				stateOfOperation = self.request.get("stateOfOperation")
				registrationNumber = self.request.get("registrationNumber")
				dateOfRegistration = self.request.get("dateOfRegistration")
				stateOfRegistration = self.request.get("stateOfRegistration")
				telephone = self.request.get("telephone")	
				address = self.request.get("address")
				dateOfRegistration  =  self.date(dateOfRegistration)
				ngo = NGO()
				ngo.userid = userid
				ngo.name = name
				ngo.credibility = False
				ngo.description = description
				ngo.pancardNumber = pancardNumber
				ngo.chiefFunctionary = chiefFunctionary
				ngo.chairman = chairman
				ngo.sectorOfOperation = sectorOfOperation
				ngo.stateOfOperation = stateOfOperation
				ngo.registrationNumber = registrationNumber
				ngo.dateOfRegistration = dateOfRegistration
				ngo.stateOfRegistration = stateOfRegistration 
				ngo.telephone = telephone 
				ngo.projects = []
				ngo.address = address 
				ngo.email = email
				ngo.put()

				index = search.Index(name = "NGO")		
				document = search.Document(doc_id = userid, fields = [ search.AtomField(name = "name", value = name ),
								       search.TextField(name = "description", value = description)])
				try:
					index.put(document)
				except search.Error:
					logging.exception("Put Failed")
				sleep(5) #cheap trick but none the less it works!
				self.redirect("/signup/ngoRegistration/proofOfRegistration")	
		else:
			self.redirect("/login") 
class ProofOfRegistration(BaseHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			userid = user.user_id()
			ngo = NGO.query(NGO.userid == userid).fetch(1)[0]
			if ngo:
				name = ngo.name
				description = ngo.description
				panCardNumber = ngo.pancardNumber
				if name and description and panCardNumber:
					upload_url = blobstore.create_upload_url("/signup/upload")
					parameter = {'upload_url':upload_url}
					self.render("ngoRegistrationUpload.html",parameter)
				else:
					self.redirect("/signup/ngoRegistration")
			else:
				self.redirect("/signup/ngoRegistration")

		else:
			self.redirect("/login")

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		user = users.get_current_user()
		if user:
			ngo = NGO.query(NGO.userid == user.user_id()).fetch(1)[0]
			if ngo:
				eightygRegistration = self.get_uploads("eightygRegistration")
				proofOfRegistration = self.get_uploads("proofOfRegistration")
				if not ngo.eightygRegistration:
					ngo.eightygRegistration = eightygRegistration[0].key() 
				if not ngo.proofOfRegistration:
					ngo.proofOfRegistration = proofOfRegistration[0].key()	
				ngo.put()
			else: 
				self.redirect("/signup/registration")
		else:
			self.redirect("/login")
		
				
app = webapp2.WSGIApplication([('/signup/userRegistration',UserRegistrationPage), ('/signup/ngoRegistration',NGORegistration),('/signup/registration',RegistrationHandler),('/signup/ngoRegistration/proofOfRegistration', ProofOfRegistration ),('/signup/upload',UploadHandler)],debug=True)	

