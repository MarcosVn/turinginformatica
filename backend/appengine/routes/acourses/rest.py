from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb
from course.course_model import CourseForm, Subject, Course
from distutils import log
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse, JsonResponse

__author__ = 'marcos'

@login_not_required
@no_csrf
def deletar(**course_id):
    key = ndb.Key(Course, int(course_id["id"]))
    key.delete()
    dct = {'id': course_id["id"]}
    return JsonUnsecureResponse(dct)


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = CourseForm(**propriedades)
    erros = form.validate()
    if erros:
        _resp.set_status(400)
        return JsonResponse(erros)
    course = form.fill_model()
    course.put()
    dct = form.fill_with_model(course)
    log.info(dct)
    return JsonResponse(dct)



@login_not_required
@no_csrf
def editar(course_id, name, duration, educationProject):
    course = Course.get_by_id(int(course_id))
    course.name = name
    course.duration = duration
    course.educationProject = educationProject
    course.put()
    form = CourseForm()
    dct = form.fill_with_model(course)
    log.info(dct)
    return JsonResponse(dct)

