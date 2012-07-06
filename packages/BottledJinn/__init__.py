# -*- coding: utf-8 -*-
from bottle import Bottle, debug, request, response, abort, redirect, static_file
from bottle.ext.redis import RedisPlugin
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
		self.install(RedisPlugin( host = 'localhost' ))
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
		@self.get( urls.models_list )
		def process_data(model_name):
			return model_name
		@self.get( urls.models_create )
		def model_new(model_name):
			return template( "admin/model_new.tpl" )
		@self.get( urls.component )
		def component( name ):
			if request.is_xhr is False:
				abort(404)
			else:
				return template( "admin/components/%s.tpl" % name )

if __name__ == '__main__':
	pass