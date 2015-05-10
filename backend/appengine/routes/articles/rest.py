from __future__ import absolute_import, unicode_literals
from article.article_model import ArticleForm
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse

__author__ = 'marcos'


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