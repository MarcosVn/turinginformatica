from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from article.article_model import ArticleForm, Article
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse

__author__ = 'marcos'

@login_not_required
@no_csrf
def deletar(**subject_id):
    key = ndb.Key(Article, int(subject_id["id"]))
    key.delete()
    dct = {'id': subject_id["id"]}
    return JsonUnsecureResponse(dct)

@login_not_required
@no_csrf
def listar():
    articles = Article.query_ordenada_por_nome().fetch()
    form= ArticleForm()
    articles = [form.fill_with_model(article) for article in articles]
    return JsonUnsecureResponse(articles)


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = ArticleForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    article = form.fill_model()
    article.put()
    dct = form.fill_with_model(article)
    log.info(dct)
    return JsonUnsecureResponse(dct)