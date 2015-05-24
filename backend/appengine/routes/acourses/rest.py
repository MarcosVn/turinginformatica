from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from course.course_model import CourseForm, Subject, Course
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse

__author__ = 'marcos'

@login_not_required
@no_csrf
def deletar(**course_id):
    key = ndb.Key(Course, int(course_id["id"]))
    key.delete()
    dct = {'id': course_id["id"]}
    return JsonUnsecureResponse(dct)

# @login_not_required
# @no_csrf
# def listar():
#     courses = Course.query_ordenada_por_nome().fetch()
#     for course in courses:
#         pass
#
#     form=CourseForm()
#     courses = [form.fill_with_model(c) for c in courses]
#     return JsonUnsecureResponse(courses)

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = CourseForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonUnsecureResponse(erros)
    course = form.fill_model()
    course.put()
    dct = form.fill_with_model(course)
    log.info(dct)
    return JsonUnsecureResponse(dct)


    # # aux vai receber o id das materias
    # aux = propriedades["subjects"]
    #
    # form = CourseForm(**propriedades)
    # erros = form.validate()
    # if erros:
    #     _resp.set_status(400)
    #     return JsonUnsecureResponse(erros)
    #
    # propriedades["subjects"] = ndb.Key(Subject, int(aux))
    #
    #
    # # Eh preciso reconstruir o form, pois o anterior jah possui propriedades soh com id onde deveria
    # # ter Key
    # form = CourseForm(**propriedades)
    # course = form.fill_model()
    # course.put()
    # dct = form.fill_with_model(course)
    # # converto a materia de Key pra id novamente (pois Key nao eh serializavel)
    # dct["subjects"] = aux
    # log.info(dct)
    # return JsonUnsecureResponse(dct)