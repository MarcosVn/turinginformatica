from google.appengine.ext import ndb
from gaeforms.base import StringField
from gaeforms.ndb.form import ModelForm

__author__ = 'marcos'

class User(ndb.Model):
    uusername = ndb.StringProperty(required=True)
    upassword = ndb.StringProperty(required=True)
    uemail = ndb.StringProperty(required=True)
    uname = ndb.StringProperty(required=True)
    ubirthday = ndb.StringProperty(required=True)
    ucriacao = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(User.uusername)

class UserForm(ModelForm):
    _model_class = User
    _include = [User.uusername]
    uusername = StringField(required=True)
    upassword = StringField(required=True)
    uemail = StringField(required=True)
    uname = StringField(required=True)
    ubirthday = StringField(required=True)