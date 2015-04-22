# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from gaeforms.base import StringField, IntegerField
from gaeforms.ndb.form import ModelForm


__author__ = 'marcos'

class Course(ndb.Model):
    name = ndb.StringProperty(required=True)
    duration = ndb.IntegerProperty(required=True)
    subjects = ndb.StringProperty(required=True)
    criacao = ndb.DateTimeProperty(auto_now_add=True)


    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Course.name)

class CourseForm(ModelForm):
    _model_class = Course
    _include = [Course.name]
    duration = IntegerField(required=True, lower=0)
    subjects = StringField(required=True)