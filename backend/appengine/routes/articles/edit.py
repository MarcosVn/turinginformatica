# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from article.article_model import Article
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes import articles
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

@no_csrf
@login_not_required
def index(article_id):
    article = Article.get_by_id(int(article_id))
    ctx={'article': article,
         'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx, 'articles/article_form.html')

@login_not_required
def atualizar(article_id, title, content, author):
    article = Article.get_by_id(int(article_id))
    article.title = title
    article.content = content
    article.author = author
    # article.img = img
    article.put()
    return RedirectResponse(articles)