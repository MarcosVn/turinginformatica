# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.base import StringField
from gaeforms.ndb.form import ModelForm


__author__ = 'marcos'

class Subject(ndb.Model):
    name = ndb.StringProperty(required=True)
    activities = ndb.StringProperty(required=True)
    criacao = ndb.DateTimeProperty(auto_now_add=True)


    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Subject.name)

class SubjectForm(ModelForm):
    _model_class = Subject
    _include = [Subject.name]
    activities = StringField(required=True)