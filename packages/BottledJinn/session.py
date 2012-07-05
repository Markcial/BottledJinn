import shelve
from BottledJinn.settings import paths, cookie
from BottledJinn.utils import generate_session_id
from bottle import request, response
import os

class Session:
	"""
	Basic session handler for the BottledJinn Framework
	"""
	def __init__(self, uuid = 'global' ):
		self.uuid = request.get_cookie( cookie.session_key, secret=cookie.secret )
		if self.uuid is None:
			self.uuid = generate_session_id()
			response.set_cookie( cookie.session_key, self.uuid, secret=cookie.secret )
		self.session_file = "%s/%s.session" % ( paths.session, self.uuid )
		self.session = shelve.open( self.session_file )

	def __getitem__(self, key):
		if self.session.has_key( key ):
			return self.session.__getitem__( key )
		else:
			return ''

	def __setitem__(self, key, value):
		self.session[key] = value

	def __delitem__(self, key):
		if self.session.has_key( key ):
			del self.session[key]

	def __iter__(self):
		return iter(self.session)

	def __len__(self):
		return len(self.session)

	def __del__(self):
		self.session.close()

	def destroy(self):
		self.session.clear()
		if os.path.exists( self.session_file ):
			os.remove( self.session_file )
