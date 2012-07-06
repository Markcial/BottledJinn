from BottledJinn import urls
from os.path import abspath,dirname

class paths:
	base = dirname( dirname( dirname( abspath( __file__ ) ) ) )
	temp = abspath(  '%s/temp' % base )
	session = abspath( '%s/session' % temp )
	templates = [
		'%s/templates' % base
	]
	auth_prefix = '/bd-admin/'
	static = abspath( '%s/static' % base )
	
class cookie:
	session_key = 'session_uuid'
	secret = 'C00k13S3cr3t'
	maxage = 30 * 24 * 60 * 60 # 30 days * 24 hours * 60 minutes * 60 seconds
	#expires = #TODO get expire time 
	#domain = # TODO get current domain
	#path =  # TODO get current path
	secure = 'off'
	httponly = 'off'

#class session:
#	type = 'file'
#	cookie_expires = 300
#	data_dir = './data'
#	auto = True

# nonce key for the user operations
nonce_key = 'bottle-djinn'

# admin user profile for basic authentication
credentials = {
	'username' : 'admin',
	'password' : 'admin'
}

class view_paths:
	base = paths.auth_prefix
	static = base + 'static'
	css = static + '/media/css'
	js = static + '/media/js'
	img = static + '/media/img'