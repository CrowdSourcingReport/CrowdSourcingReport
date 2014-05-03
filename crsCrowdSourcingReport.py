#oggpnosn
#hkhr
import webapp2
from google.appengine.ext import ndb

class Task(ndb.Model):
    problemStatement=ndb.StringProperty(indexed=False)
    fund=ndb.FloatProperty()
    contributor=ndb.JsonProperty(indexed=True)
    status=ndb.BooleanProperty()
    projectName=ndb.StringProperty(indexed=False)
class Project(ndb.Model):
    taskList=ndb.JsonProperty()
    projectManager=ndb.StringProperty(indexed=False)


webText="""<!DOCTYPE html>
<html>

<body>
<h1 style="text-align:center;">Home Page</h1>
<div align="center">
<table style="text-align:center">
<tr>
  <td style="background-color:#C0C0C0"><a href="/manager">Manager</a></td>
  </tr>
<tr>
  <td></td>
</tr>

<tr>
  <td style="background-color:#C0C0C0"><a href=/organization>Organization</a></td>
  </tr>
<tr>
  <td></td>
</tr>

</table>
</div>
</body>

</html>
 """
managerText="""<!DOCTYPE html>
<html>

<body>
<h1 style="text-align:center;">Manager Dashboard</h1>
<div align="middle">
<table style="text-align:center">
<tr>
  <td style="background-color:#C0C0C0"><a href="/manager/newProject">Create New Project</a></td>
  </tr>
<tr>
  <td></td>
</tr>

<tr>
  <td style="background-color:#C0C0C0"><a href=/manager/updateProject>Update Existing Project</a></td>
  </tr>
<tr>
  <td></td>
</tr>

</table>
</div>
</body>

</html> """

newProjectTextInitial="""<!DOCTYPE html>
<html>

<body>
<h3 style="margin-left:50px">Add New Project</h1>
<p style="margin-left:50px"><b>Enter Details Below</b></p>
<div style="margin-left:50px">
<form action="/manager/addProject/addTask" method="post">
<fieldset>
<p><b>Project Details</b></p><p>
          <label>Project Name</label><br>
          <textarea name="projectName" rows="1" cols="40">%s</textarea>
</p>   
<p>
   <label>Project Description</label><br>
   <textarea name="projectDescription" rows="4" cols="80">%s</textarea>
</p>
<p>
   <label>Number Of Tasks</label><br>
   <input type = "number" id = "numberOfTasks" name="noOfTasks"style="width:50px"/>
 </p>
</fieldset><br>
 <input type="submit" value="Send"><input type="reset">
</form>
</div>
</body>

</html> """
newProjectTextFinal=""" <!DOCTYPE html>
<html>

<body>
<h3 style="margin-left:50px">Add New Project</h1>
<p style="margin-left:50px"><b>Enter Details Below</b></p>
<div style="margin-left:50px">
<form action="/manager" method="post">
<fieldset>
<p><b>Project Details</b></p><p>
          <label>Project Name</label><br>
          <textarea name="projectName" rows="1" cols="40">%s
   </textarea>
</p>   
<p>
   <label>Project Description</label><br>
   <textarea name="projectDescription" rows="4" cols="80">%s
   </textarea>
</p>
<p>
   <label>Number Of Tasks</label><br>
   <input type = "number" id = "numberOfTasks" style="width:50px"/>
 </p>
</fieldset><br>
 """
taskDetailText=""" <fieldset>
<p><b>Task Details</b></p>
<p>
   <label>Description</label><br>
<textarea name="desc%s" rows="2" cols="80"></textarea><br> 
</p>
<p>   <label>Fund Required</label><br>
<input ty pe = "number" id = "fund" style="width:100px"/>
 </p>
<p style="text-align:right"><a href="">Next</a></p>
</fieldset><br>
"""
class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(webText)

class Manager(webapp2.RequestHandler):

   def get(self):
       self.response.headers['Content-Type'] = 'text/html'
       self.response.write(managerText)
   def post(self):
       problemStatement=self.request.get("projectDescription")
       projectName=self.request.get("projectName")
       fund=self.request.get("Name")
       noOfTasks=self.request.get("noOfTasks")
       descr=[]
       for i in range(noOfTasks):
           descr.append(self.request.get("desc"+str(i+1)))
       
       self.response.headers['Content-Type'] = 'text/html'
       self.response.write(managerText)
     
class Organization(webapp2.RequestHandler):

   def get(self):
       self.response.headers['Content-Type'] = 'text/html'
       self.response.write(webText)

class NewProject (webapp2.RequestHandler):
   def get(self):
       self.response.headers['Content-Type'] = 'text/html'
       self.response.write(newProjectTextInitial%("",""))
       
class AddTask(webapp2.RequestHandler):
   def post(self):
       projectDescription=self.request.get("projectDescription")
       projectName=self.request.get("projectName")
       noOfTask=int(self.request.get("noOfTasks"))
       self.response.write(newProjectTextFinal%(projectName,projectDescription))
       for i in range(noOfTask):
           self.response.write(taskDetailText%(i+1))
       self.response.write("""  <input type="submit" value="Send"><input type="reset">
</FORM>
</div>
</body>
</html>""")

         
 
class UpdateProject (webapp2.RequestHandler):
   def get(self):
       self.response.headers['Content-Type'] = 'text/html'
       self.response.write(webText)
  

application = webapp2.WSGIApplication([
    ('/', MainPage),('/manager',Manager),('/organization',Organization),('/manager/newProject',NewProject),('/manager/updateProject',UpdateProject),("/manager/addProject/addTask",AddTask)
], debug=True)
