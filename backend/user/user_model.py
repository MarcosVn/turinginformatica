# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

__author__ = 'marcos'



class User(ndb.Model):
    id = ndb.IndexProperty()
    login = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    logged = ndb.BooleanProperty()

    @classmethod
    def query_all_ordered_by_name(cls):
        return cls.query_all_ordered_by_name(User.name)


    @classmethod
    def query_all_ordered_by_id(cls):
        return cls.query_all_ordered_by_id(User.id)




