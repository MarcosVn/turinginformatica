# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


__author__ = 'marcos'


class Subject(ndb.Model):
    title = ndb.StringProperty(required=True)


    @classmethod
    def query_all_ordered_by_name(cls):
        return cls.query_all_ordered_by_name(Subject.title)


