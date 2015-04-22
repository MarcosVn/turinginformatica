# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from article.article_model import Article, ArticleForm
from config.template_middleware import TemplateResponse
from routes import articles
from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'marcos'

def salvar(**kwargs):
    form = ArticleForm(**kwargs)
    erros = form.validate()
    if not erros:
        properties = form.normalize()
        article = Article(**properties)
        article.put()
        return RedirectResponse(articles)

    else:
        ctx = {'articles': kwargs, 'erros': erros}
        return TemplateResponse(ctx, 'articles/article_form.html')