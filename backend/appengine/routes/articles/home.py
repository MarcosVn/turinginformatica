# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from article.article_model import Article
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import ADMIN
from routes.articles import edit
from routes.articles.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

# @permissions(ADMIN)
@no_csrf
def index():
    query = Article.query_ordenada_por_nome()
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)
    articles = query.fetch()
    for a in articles:
        key = a.key
        key_id = key.id()
        a.edit_path = to_path(edit_path_base, key_id)
        a.deletar_path = to_path(deletar_path_base, key_id)
    ctx = {'salvar_path': to_path(salvar),
           'articles': articles}

    return TemplateResponse(ctx, 'articles/article_home.html')

def deletar(article_id):
    key = ndb.Key(Article, int(article_id))
    key.delete()
    return RedirectResponse(index)

