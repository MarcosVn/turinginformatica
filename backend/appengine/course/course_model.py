# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from gaeforms.base import StringField, IntegerField
from gaeforms.ndb.form import ModelForm

__author__ = 'marcos'


class Subject(ndb.Model):
    name = ndb.StringProperty(required=True)
    activities = ndb.StringProperty(required=True)
    criacao = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Subject.name)

    @classmethod
    def query_ordenada_por_id(cls):
        return cls.query().order(Subject.get_by_id)


class SubjectForm(ModelForm):
    _model_class = Subject
    _include = [Subject.name]
    activities = StringField(required=True)

class Course(ndb.Model):
    name = ndb.StringProperty(required=True)
    duration = ndb.StringProperty(required=True)
    subjects = ndb.KeyProperty(Subject, required=True)
    criacao = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Course.name)

    @classmethod
    def query_ordenada_por_subjects(cls, subject_selecionado):
        if isinstance(subject_selecionado, basestring):
            subject_selecionado = ndb.Key(Subject, int(subject_selecionado))
        return cls.query(cls.subjects == subject_selecionado).order(cls.name)


class CourseForm(ModelForm):
    _model_class = Course
    _include = [Course.name]
    duration = StringField(required=True)
    subjects = StringField(required=True)


