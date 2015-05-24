from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from course.course_model import SubjectForm, Subject, Course
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse

__author__ = 'marcos'

@login_not_required
@no_csrf
def deletar(**subject_id):
    key = ndb.Key(Subject, int(subject_id["id"]))
    key.delete()
    dct = {'id': subject_id["id"]}
    return JsonUnsecureResponse(dct)

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    # form = SubjectForm(**propriedades)
    # erros = form.validate()
    # if erros:
    #     _resp.set_status(400)
    #     return JsonUnsecureResponse(erros)
    # subject = form.fill_model()
    # subject.put()
    # dct = form.fill_with_model(subject)
    # log.info(dct)
    # return JsonUnsecureResponse(dct)

    # aux vai receber o id do curso
    aux = propriedades["course"]
    form = SubjectForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)

    propriedades["course"] = ndb.Key(Course, int(aux))

    # Eh preciso reconstruir o form, pois o anterior jah possui propriedades soh com id onde deveria
    # ter Key
    form = SubjectForm(**propriedades)
    subject = form.fill_model()
    subject.put()
    dct = form.fill_with_model(subject)
    # converto o curso de Key pra id novamente (pois Key nao eh serializavel)
    dct["course"] = aux
    log.info(dct)
    return JsonUnsecureResponse(dct)


