# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from course.course_model import Course
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import ADMIN
from routes.acourses import edit
from routes.acourses.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

@permissions(ADMIN)
@no_csrf
def index():
    query = Course.query_ordenada_por_nome()
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)
    courses = query.fetch()

    for course in courses:
        key = course.key
        key_id = key.id()
        course.edit_path = to_path(edit_path_base, key_id)
        course.deletar_path = to_path(deletar_path_base, key_id)

    ctx = {'courses': courses,
           'salvar_path': to_path(salvar)}

    return TemplateResponse(ctx, 'acourses/courses_home.html')

def deletar(course_id):
    key = ndb.Key(Course, int(course_id))
    key.delete()
    return RedirectResponse(index)
