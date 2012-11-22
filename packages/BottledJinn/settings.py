from os.path import abspath, dirname


class AttrDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class paths(AttrDict):
    base = dirname(dirname(dirname(abspath(__file__))))
    temp = abspath('%s/temp' % base)
    session = abspath('%s/session' % temp)
    data = abspath('%s/data' % base)
    data_file = abspath('%s/models.pk' % data)
    templates = [
        '%s/templates' % base
    ]
    auth_prefix = '/admin/'
    static = abspath('%s/static' % base)


class cookie:
    session_key = 'session_uuid'
    secret = 'C00k13S3cr3t'
    maxage = 30 * 24 * 60 * 60  # 30 days * 24 hours * 60 minutes * 60 seconds
    #expires = #TODO get expire time
    #domain = # TODO get current domain
    #path =  # TODO get current path
    secure = 'off'
    httponly = 'off'

#class session:
#    type = 'file'
#    cookie_expires = 300
#    data_dir = './data'
#    auto = True

# nonce key for the user operations
nonce_key = 'bottled-jinn'

# admin user profile for basic authentication
credentials = {
    'username': 'admin',
    'password': 'admin'
}


class view_paths:
    base = paths.auth_prefix
    static = base + 'static'
    css = static + '/media/css'
    js = static + '/media/js'
    img = static + '/media/img'


urls = AttrDict({
    "login": '/login',
    "logout": '/logout',
    "dashboard": '/dashboard',
    "static": '/static/<filename:path>',
    "models_design": '/data/design',
    "models_list": '/data/<model_name:re:[a-z0-9-_]+>/list',
    "models_create": '/data/<model_name:re:[a-z0-9-_]+>/new',
    "models_edit": '/data/<model_name:re:[a-z0-9-_]+>/edit/<id:int>',
    "models_delete": '/data/<model_name:re:[a-z0-9-_]+>/delete/<id:int>'
})
