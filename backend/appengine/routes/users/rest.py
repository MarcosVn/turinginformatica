from __future__ import absolute_import, unicode_literals
from course.course_model import SubjectForm
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required, login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse
from user.user_model import UserForm

__author__ = 'marcos'


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = UserForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    user = form.fill_model()
    user.put()
    dct = form.fill_with_model(user)
    log.info(dct)
    return JsonUnsecureResponse(dct)