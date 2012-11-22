# -*- coding: utf-8 -*-
from bottle import Bottle, request, redirect, static_file
from bottle.ext.redis import RedisPlugin
from BottledJinn.settings import *
from BottledJinn.utils import *
from BottledJinn.session import Session
from BottledJinn.models import Field, Model
from BottledJinn.auth import AuthPlugin, authenticate
from jinja2 import Environment, FileSystemLoader, TemplateNotFound


class Jinn(Bottle):

    def __init__(self, catchall=True, autojson=True):
        super(Jinn, self).__init__(catchall, autojson)

        def template(name, **ctx):
            tpl = self.jinja2_env.get_template(name)
            ctx['env'] = request.environ
            ctx['paths'] = view_paths
            ctx['urls'] = urls
            ctx['url'] = self.get_url
            return tpl.render(**ctx)

        self.install(AuthPlugin())
        self.install(RedisPlugin(host='localhost'))
        self.jinja2_env = Environment(
            loader=FileSystemLoader(paths.templates),
            cache_size=0
        )

        @self.hook('before_request')
        def before_request():
            self.session = Session()

        @self.get('/', skip=[AuthPlugin])
        @self.get(urls.login, skip=[AuthPlugin])
        def login():
            if self.session['authenticated'] is True:
                redirect(self.get_url(urls.dashboard))
            else:
                return template(
                    "admin/login.tpl",
                    login_url=self.get_url(urls.login)
                )

        @self.post(urls.login, skip=[AuthPlugin])
        def post_login():
            username = request.forms.get('user')
            password = request.forms.get('password')
            if authenticate(username, password) is True:
                redirect(self.get_url(urls.dashboard))
            else:
                redirect(self.get_url(urls.login))

        @self.get(urls.logout)
        def get_logout():
            self.session.destroy()
            redirect(self.get_url(urls.login))

        @self.get(urls.dashboard)
        def dashboard(rdb):
            models = []
            obj = rdb.hgetall('models')
            for itm in obj:
                model = Model.from_json(obj[itm])
                models.append(model)
            return template("admin/dashboard.tpl", models=models)

        @self.get(urls.static, skip=[AuthPlugin])
        def serve_static(filename):
            return static_file(filename, root=paths.static)

        @self.get(urls.models_list)
        def process_data(model_name):
            return model_name

        @self.get(urls.models_create)
        def model_new(model_name, rdb):
            jsmodel = rdb.hget('models', model_name)
            model = Model.from_json(jsmodel)
            return template(
                    "admin/model_new.tpl",
                    model_name=model_name,
                    model=model
            )

        @self.post(urls.models_create)
        def model_save(model_name, rdb):
            jsmodel = rdb.hget('models', model_name)
            model = Model.from_json(jsmodel)
            for f in model.fields:
                f.value = request.forms.get(f.name)
            index = rdb.lpush(
                "%s::%s" % ("models", model_name),
                model.__json__()
            )
            redirect(
                self.get_url(urls.models_edit, model_name=model_name, id=index)
            )

        @self.get(urls.models_list)
        def models_list(model_name, rdb):
            models = []
            obj = rdb.hgetall('models')
            for itm in obj:
                model = Model.from_json(obj[itm])
                models.append(model)
            jsmodel = rdb.hget('models', model_name)
            model = Model.from_json(jsmodel)
            item_list = rdb.lrange("%s::%s" % ("models", model_name), 0, 10)
            items = []
            for a in item_list:
                items.append(Model.from_json(a))
            return template(
                "admin/model_list.tpl",
                model_name=model_name,
                model=model,
                models=models,
                items=items
            )

        @self.get(urls.models_design)
        def model_design():
            return template("admin/model_design.tpl")

        @self.post(urls.models_design)
        def model_design_save(rdb):
            model_name = request.POST.get('model_name')
            types = request.POST.getall('type[]')
            labels = request.POST.getall('label[]')
            names = request.POST.getall('name[]')
            ids = request.POST.getall('id[]')
            orders = request.POST.getall('order[]')
            values = request.POST.getall('values[]')
            fields = []
            for a in range(0, len(types)):
                field = Field(
                    names[a],
                    types[a],
                    labels[a],
                    ids[a],
                    orders[a],
                    values[a] if a in values else ''
                )
                fields.append(field)
            model = Model(model_name, fields)
            rdb.hset('models', model.name, model.__json__())
            redirect(self.get_url(urls.models_list, model_name=model_name))

        @self.get(urls.models_edit)
        def model_edit(model_name, id, rdb):
            jsmodel = rdb.lindex("%s::%s" % ("models", model_name), id - 1)
            model = Model.from_json(jsmodel)
            return template(
                    "admin/model_new.tpl",
                    model_name=model_name,
                    model=model
            )

if __name__ == '__main__':
    pass
