# -*- coding: utf-8 *-*
try:
    import json
except ImportError:
    import simplejson as json


class Field(object):

    def __init__(self, name, type, label, id, order, value=False):
        self.name = name
        self.type = type
        self.label = label
        self.id = id
        self.order = order
        self.value = value

    def __repr__(self):
        return str(self.__dict__)

    __str__ = __repr__

    def __json__(self):
        return json.dumps(self.__dict__)


class Model(object):

    def __init__(self, name, fields=[]):
        self.name = name
        self.fields = fields

    def __repr__(self):
        return str(self.__dict__)

    __str__ = __repr__

    def __json__(self):
        return json.dumps({
            "name": self.name,
            "fields": [field.__dict__ for field in self.fields]
        })

    @staticmethod
    def from_json(js):
        jsob = json.loads(js)
        fields = []
        for jsf in jsob['fields']:
            fields.append(
                Field(
                    jsf['name'],
                    jsf['type'],
                    jsf['label'],
                    jsf['id'],
                    jsf['order'],
                    jsf['value'] if 'value' in jsf else ''
                )
            )
        return Model(jsob['name'], fields)
