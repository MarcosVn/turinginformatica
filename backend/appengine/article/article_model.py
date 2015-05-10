from google.appengine.ext import ndb

from gaeforms.base import StringField
from gaeforms.ndb.form import ModelForm

__author__ = 'marcos'

class Article(ndb.Model):
    title = ndb.StringProperty(required=True)
    content = ndb.StringProperty(required=True)
    author = ndb.StringProperty(required=True)
    img = ndb.BlobProperty()
    criacao = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Article.title)

class ArticleForm(ModelForm):
    _model_class = Article
    _include = [Article.title]
    title = StringField(required=True)
    content = StringField(required=True)
    author = StringField(required=True)