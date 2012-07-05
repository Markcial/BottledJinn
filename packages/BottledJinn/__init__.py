# -*- coding: utf-8 -*-
from bottle import Bottle, debug, request, response, redirect, static_file
from BottledJinn.settings import *
from BottledJinn.utils import *
from BottledJinn.session import Session
from BottledJinn.auth import AuthPlugin, authenticate
from jinja2 import Environment, FileSystemLoader

class Jinn(Bottle):
	def __init__(self, catchall=True, autojson=True):
		super(Jinn, self).__init__(catchall, autojson )
		def template( name, **ctx ):
			tpl = self.jinja2_env.get_template(name)
			ctx[ 'env' ] = request.environ
			ctx[ 'paths' ] = view_paths
			return tpl.render(**ctx)
		self.mount( paths.auth_prefix ,self )
		self.install(AuthPlugin())
		self.jinja2_env = Environment(loader=FileSystemLoader(paths.templates), cache_size=0)
		@self.hook('before_request')
		def before_request():
			self.session = Session()
		#	if self.session[ 'authenticated' ] is not True and request.environ['PATH_INFO'] != urls.login:
		#		redirect( self.get_url( urls.login ) )
		@self.get( '/', skip=[AuthPlugin] )
		@self.get( urls.login, skip=[AuthPlugin] )
		def login():
			return template( "admin/login.tpl", login_url=self.get_url( urls.login ) )
		@self.post( urls.login, skip=[AuthPlugin] )
		def post_login():
			username = request.forms.get( 'user' )
			password = request.forms.get( 'password' )
			if authenticate( username, password ) is True:
				redirect( self.get_url( urls.dashboard ) )
			else:
				redirect( self.get_url( urls.login ) )
		@self.get( urls.logout )
		def get_logout():
			self.session.destroy()
			redirect( self.get_url( urls.login ) )
		@self.get( urls.dashboard )
		def dashboard():
			return template( "admin/dashboard.tpl" )
		@self.get( urls.static, skip=[AuthPlugin] )
		def serve_static( filename ):
			return static_file(filename, root=paths.static )

if __name__ == '__main__':
	pass

#"""
#from bottle import Bottle, mount, run, debug
#from BottleDjinn.settings import *
#from BottleDjinn.auth import *
#from BottleDjinn.utils import *
#from beaker.middleware import SessionMiddleware#
#
#app = Bottle()
#mount( realm_prefix, app )
#
# basic login
#@app.route( '/login', method= 'GET' )
#def login():#
#	return template( 'admin/login.tpl', login_url=app.get_url('/login') )
#	
#@app.route( '/login', method= 'POST' )
#def login():
#	# authenticate
#	# if ok then dashboard
#	name = request.forms.get('name')
#	password = request.forms.get('password')
#	nonce = request.forms.get('nonce')
#	creds = True
#	if creds is True:
#		redirect( app.get_url( '/dashboard' ) )
#	else:
#		redirect( app.get_url( '/login' ) )
#		
#@app.route( '/dashboard' )
#def dashboard():
#	return template( 'admin/dashboard.tpl' )
#
#
#session_opts = {
#	'session.type': 'file',
#	'session.cookie_expires': 300,
#	'session.data_dir': './data',
#	'session.auto': True
#}
#app = SessionMiddleware(app, session_opts)
#debug( True )
#run(app=app,reloader=True,host='localhost', port=8080)
#"""