from bottle import redirect

class AuthPlugin(object):
	def setup( self, app ):
		self.app = app
	def apply(self, callback, route ):
		def wrapper(*args,**kwargs):
			from BottledJinn.session import Session
			from BottledJinn.settings import urls 
			from bottle import redirect
			session = Session()
			if session['authenticated'] is not True:
				redirect( self.app.get_url( urls.login ) )
			rv = callback(*args, **kwargs)
			return rv
		return wrapper

def authenticate( username, password ):
	from BottledJinn.settings import credentials
	from BottledJinn.session import Session
	if credentials['username'] == username and credentials['password'] == password:
		session = Session()
		session['authenticated'] = True
		return True
	return False

def create_nonce( seed ):
	pass

def verify_nonce( seed ):
	pass
