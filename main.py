#oggpnosn
#hkhr
#script to implement signup

# things to do: Signup is working. Add the link for email verification. Login should work... but is said that there is a problem in my imported security.py file Please check
# display_message is an unnecessary method. I have kept it to check if the various functions are working
# wherever called, replace it with self.response.write(self.render_template('html file you want to render', any message)


#importing essential library-----------------
from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from webapp2_extras import security
import logging
import os.path
import webapp2
import re
from webapp2_extras import auth
from webapp2_extras import sessions
from webapp2_extras.auth import InvalidAuthIdError
from webapp2_extras.auth import InvalidPasswordError

#check if a user associated with the current session exists
def user_required(handler):
  """
    Decorator that checks if there's a user associated with the current session.
    Will also fail if there's no session present.
  """
  def check_login(self, *args, **kwargs):
    auth = self.auth
    if not auth.get_user_by_session():
      self.redirect(self.uri_for('login'), abort=True)
    else:
      return handler(self, *args, **kwargs)

  return check_login

#basic tools needed
class BaseHandler(webapp2.RequestHandler):
  #access auth instances as a property
  @webapp2.cached_property
  def auth(self):
    """Shortcut to access the auth instance as a property."""
    return auth.get_auth()

  #access information about the user which is stored in the session
  @webapp2.cached_property
  def user_info(self):
    """Shortcut to access a subset of the user attributes that are stored
    in the session.

    The list of attributes to store in the session is specified in
      config['webapp2_extras.auth']['user_attributes'].
    :returns
      A dictionary with most user information
    """
    return self.auth.get_user_by_session()

  #access the user currently logged in
  @webapp2.cached_property
  def user(self):
    """Shortcut to access the current logged in user.

    Unlike user_info, it fetches information from the persistence layer and
    returns an instance of the underlying model.

    :returns
      The instance of the user model associated to the logged in user.
    """
    u = self.user_info
    return self.user_model.get_by_id(u['user_id']) if u else None

  #accessing the user model
  @webapp2.cached_property
  def user_model(self):
    """Returns the implementation of the user model.

    It is consistent with config['webapp2_extras.auth']['user_model'], if set.
    """    
    return self.auth.store.user_model

  #accessing the current session
  @webapp2.cached_property
  def current_session(self):
      """Shortcut to access the current session."""
      return self.session_store.get_session(backend="datastore")

  #accessing the templates
  def render_template(self, view_filename, params=None):
    if not params:
      params = {}
    user = self.user_info
    params['user'] = user
    path = os.path.join(os.path.dirname(__file__), 'Content/html', view_filename)
    self.response.out.write(template.render(path, params))

  #displaying required messages
  def display_message(self, message):
    """Utility function to display a template with a simple message."""
    params = {
      'message': message
    }
    self.render_template('message.html', params)

  #implementing webapp2 sessions
  def dispatch(self):
      #obtaining a session
      self.session_store = sessions.get_store(request=self.request)
      try:
          #dispatch the request.
          webapp2.RequestHandler.dispatch(self)
      finally:
          #save all sessions.
          self.session_store.save_sessions(self.response)

#standard string definition
emailAlertMessage="Kindly enter a valid email!"	
passwordAlertMessage="Password can cointain a-z, A-Z, 0-9, _ and - only, and a length in between 6 and 20"
usernameAlertMessage="Username can cointain a-z, A-Z, 0-9, _ and - only, and a length in between 6 and 20"
confirmPasswordAlertMessage="Password does not match!"
inputWarning="inputWarning"

#initializing regular expression checker for email,password and username
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{6,20}$")
PASS_RE=re.compile(r"^[a-zA-Z0-9_-]{6,20}$")
EMAIL_RE=re.compile(r"^[\S]+@[\S]+\.[\S]+$")

#implementing password confirmation check
def verify_password(password,verify):
	if password==verify:
		return True
	else:
		return False

#implementing check for validity of password
def valid_password(password):
	ret=PASS_RE.match(password)
	if ret==None:
		return False
	else:
		return True

#implementing check for validity of username
def valid_username(username):
	ret=USER_RE.match(username)
	if ret==None:
                return False
        else:
                return True

#implementing check for validity of email
def valid_email(email):
        ret= EMAIL_RE.match(email)
	if ret==None:
                return False
        else:
                return True

#creating a new user account
class SignupHandler(BaseHandler):
  def get(self):
    self.render_template('signup.html')

  def post(self):
    name=self.request.get("name")
    username=self.request.get("username")
    password=self.request.get("password")
    confirmPassword=self.request.get("confirmPassword")
    emailId=self.request.get("emailId")

    #boolean to store validity of email,password and username
    emailValidity=valid_email(emailId)
    passwordValidity=valid_password(password)
    usernameValidity=valid_username(username)
    confirmPasswordValidity=verify_password(password,confirmPassword)

    #if all the validity condition are passed then move on to storing data 
    if emailValidity and passwordValidity and usernameValidity and confirmPasswordValidity:
      unique_properties = ['email_address']
      user_data = self.user_model.create_user(username,unique_properties,email_address=emailId, name=name, raw_password=password,verified=False)
      if not user_data[0]: #user_data is a tuple
        self.display_message('Unable to create user for email %s because of \duplicate keys %s' % (username, user_data[1]))
        return
      user = user_data[1]
      user_id = user.get_id()
      token = self.user_model.create_signup_token(user_id)
      #verifying email address
      verification_url = self.uri_for('verification', type='v', user_id=user_id,signup_token=token, _full=True)
      msg = 'Send an email to user in order to verify their address. \They will be able to do so by visiting <a href="{url}">{url}</a>'
      self.display_message(msg.format(url=verification_url))

    #otherwise generate appropriate error message to help user through registration process
    else:
      alertMessage={}
      if not emailValidity:
        alertMessage["emailAlertMessage"]=emailAlertMessage
      if not usernameValidity:
        alertMessage["usernameAlertMessage"]=usernameAlertMessage
      if not passwordValidity:
        alertMessage["passwordAlertMessage"]=passwordAlertMessage
      if not confirmPasswordValidity:
        alertMessage["confirmPasswordAlertMessage"]=confirmPasswordAlertMessage
      alertMessage["inputWarningPassword"]=inputWarning
      self.response.write(self.render_template('signup.html',alertMessage))

#if user forgets his password
class ForgotPasswordHandler(BaseHandler):
  def get(self):
    self._serve_page()

  def post(self):
    username = self.request.get('username')

    user = self.user_model.get_by_auth_id(username)
    if not user:
      logging.info('Could not find any user entry for username %s', username)
      self._serve_page(not_found=True)
      return

    user_id = user.get_id()
    token = self.user_model.create_signup_token(user_id)

    verification_url = self.uri_for('verification', type='p', user_id=user_id,
      signup_token=token, _full=True)

    msg = 'Send an email to user in order to reset their password. \
          They will be able to do so by visiting <a href="{url}">{url}</a>'

    self.display_message(msg.format(url=verification_url))
  
  def _serve_page(self, not_found=False):
    username = self.request.get('username')
    params = {
      'username': username,
      'not_found': not_found
    }
    self.render_template('forgot.html', params)

#verifying a user
class VerificationHandler(BaseHandler):
  def get(self, *args, **kwargs):
    user = None
    user_id = kwargs['user_id']
    signup_token = kwargs['signup_token']
    verification_type = kwargs['type']
    user, ts = self.user_model.get_by_auth_token(int(user_id), signup_token,'signup')

    if not user:
      logging.info('Could not find any user with id "%s" signup token "%s"',user_id, signup_token)
      self.abort(404)
    
    # store user data in the session
    self.auth.set_session(self.auth.store.user_to_dict(user), remember=True)

    if verification_type == 'v':
      # remove signup token, we don't want users to come back with an old link
      self.user_model.delete_signup_token(user.get_id(), signup_token)

      if not user.verified:
        user.verified = True
        user.put()

      self.display_message('User email address has been verified.')
      return
    elif verification_type == 'p':
      # supply user to the page
      params = {
        'user': user,
        'token': signup_token
      }
      self.render_template('resetpassword.html', params)
    else:
      logging.info('verification type not supported')
      self.abort(404)

#setting the new password
class ResetPasswordHandler(BaseHandler):
  @user_required
  def post(self):
    password = self.request.get('password')
    old_token = self.request.get('t')

    if not password or password != self.request.get('confirm_password'):
      self.display_message('passwords do not match')
      return

    user = self.user
    user.set_password(password)
    user.put()

    # remove signup token, we don't want users to come back with an old link
    self.user_model.delete_signup_token(user.get_id(), old_token)
    
    self.display_message('Password updated')

#logging in an existing user
class LoginHandler(BaseHandler):
  def get(self):
    self._serve_page()

  def post(self):
    username = self.request.get('username')
    password = self.request.get('password')
    try:
      u = self.auth.get_user_by_password(username, password, remember=True,
        save_session=True)
      self.redirect(self.uri_for('home'))
    except (InvalidAuthIdError, InvalidPasswordError) as e:
      logging.info('Login failed for user %s because of %s', username, type(e))
      self._serve_page(True)

  def _serve_page(self, failed=False):
    username = self.request.get('username')
    params = {
      'username': username,
      'failed': failed
    }

#page to be opened after logging in.. temporary
class LoggedInUserHandler(BaseHandler):
        def get(self):
                self.render_template('project_page.html')

#logging out
class LogoutHandler(BaseHandler):
  def get(self):
    self.auth.unset_session()
    self.redirect('/')

#successful login
class AuthenticatedHandler(BaseHandler):
  @user_required
  def get(self):
    self.render_template('authenticated.html')

config = {
  'webapp2_extras.auth': {
    'user_model': 'models.User',
    'user_attributes': ['name']
  },
  'webapp2_extras.sessions': {
    'secret_key': 'YOUR_SECRET_KEY'
  }
}

app = webapp2.WSGIApplication([
    webapp2.Route('/user', LoggedInUserHandler), 
    webapp2.Route('/signup', SignupHandler, name = 'home'),
    webapp2.Route('/<type:v|p>/<user_id:\d+>-<signup_token:.+>',
      handler=VerificationHandler, name='verification'),
    webapp2.Route('/password', ResetPasswordHandler),
    webapp2.Route('/login', LoginHandler, name='login'),
    webapp2.Route('/logout', LogoutHandler, name='logout'),
    webapp2.Route('/forgot', ForgotPasswordHandler, name='forgot'),
    webapp2.Route('/authenticated', AuthenticatedHandler, name='authenticated')
], debug=True, config=config)

logging.getLogger().setLevel(logging.DEBUG)
