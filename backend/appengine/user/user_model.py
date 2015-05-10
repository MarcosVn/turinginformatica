from google.appengine.ext import ndb
from gaeforms.base import StringField
from gaeforms.ndb.form import ModelForm

__author__ = 'marcos'

class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    birthday = ndb.StringProperty(required=True)
    criacao = ndb.DateTimeProperty(auto_now_add=True)


    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(User.username)

    @classmethod
    def query_ordenada_por_criacao(cls):
        return cls.query().order(User.criacao)

class UserForm(ModelForm):
    _model_class = User
    _include = [User.username]
    password = StringField(required=True)
    email = StringField(required=True)
    name = StringField(required=True)
    birthday = StringField(required=True)