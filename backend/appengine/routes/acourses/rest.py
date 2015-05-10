from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb

from course.course_model import CourseForm, Subject
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse


__author__ = 'marcos'


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    # aux vai receber o id das materias
    aux = propriedades["subjects"]

    form = CourseForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)

    propriedades["subjects"] = ndb.Key(Subject, int(aux))
    # Eh preciso reconstruir o form, pois o anterior jah possui propriedades soh com id onde deveria
    # ter Key
    form = CourseForm(**propriedades)
    course = form.fill_model()
    course.put()
    dct = form.fill_with_model(course)
    # converto a materia de Key pra id novamente (pois Key nao eh serializavel)
    dct["subjects"] = aux
    log.info(dct)
    return JsonUnsecureResponse(dct)