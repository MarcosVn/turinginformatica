# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
__author__ = 'marcos'

class Course(ndb.Model):
    name = ndb.StringProperty(required=True)
    duration = ndb.StringProperty(required=True)


    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query_ordenada_por_nome(Course.name)





