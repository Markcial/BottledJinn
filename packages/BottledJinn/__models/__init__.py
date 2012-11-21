# -*- coding: utf-8 -*-
"""
import shelve
from BottledJinn.settings import paths


class Field(object):

    def __init__(self, name, type, label, value=False):
        self.name = name
        self.type = type
        self.label = label
        self.value = value


class Model(object):

    def __init__(self, name, fields=[]):
        self.name = name
        self.fields = fields


class ModelManager(object):

    def __init__(self):
        super(ModelManager, self).__init__()
        self.shelf = shelve.open(paths.data_file)
        print self.shelf
        if 'models' not in self.shelf:
            self.shelf['models'] = {}
        self.models = self.shelf['models']

    def save_model(self, model):
        self.shelf['models'][model.name] = model

    def save_models(self, models):
        self.shelf['models'] = models

    def get_model(self, name):
        return self.shelf['models'][name]

    def get_models(self):
        return self.models
"""
