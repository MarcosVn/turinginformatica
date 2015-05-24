from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.base import StringField, IntegerField
from gaeforms.ndb.form import ModelForm

__author__ = 'marcos'

class Course(ndb.Model):
    name = ndb.StringProperty(required=True)
    duration = ndb.StringProperty(required=True)
    educationProject = ndb.StringProperty(required=True)
    criacao = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Course.name)


class CourseForm(ModelForm):
    _model_class = Course
    _include = [Course.name]
    duration = StringField(required=True)
    educationProject = StringField(required=True)

class Subject(ndb.Model):
    name = ndb.StringProperty(required=True)
    activities = ndb.StringProperty(required=True)
    course = ndb.KeyProperty(Course, required=True)
    criacao = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Subject.name)

    @classmethod
    def query_ordenada_por_courses(cls, course_selecionado):
        if isinstance(course_selecionado, basestring):
            course_selecionado = ndb.Key(Course, int(course_selecionado))
        return cls.query(cls.course == course_selecionado).order(cls.name)


class SubjectForm(ModelForm):
    _model_class = Subject
    _include = [Subject.name]
    activities = StringField(required=True)
    course = StringField(required=True)




