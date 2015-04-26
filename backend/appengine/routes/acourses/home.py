# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from course.course_model import Course, Subject
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import ADMIN
from routes.acourses import edit
from routes.acourses.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

# @permissions(ADMIN)
@no_csrf
def index(subject_selecionado = None):

    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)
    ctx = {'subjects': Subject.query_ordenada_por_nome().fetch(),
           'salvar_path': to_path(salvar)}

    if subject_selecionado is None:
        ctx['courses'] = Course.query_ordenada_por_nome().fetch()
        ctx['subject_selecionado'] = None


    else:
        ctx['subject_selecionado'] = Subject.get_by_id(int(subject_selecionado))
        ctx['courses']= Course.query_ordenada_por_subjects(subject_selecionado).fetch()


    for course in ctx['courses']:
        key = course.key
        key_id = key.id()
        course.edit_path = to_path(edit_path_base, key_id)
        course.deletar_path = to_path(deletar_path_base, key_id)


    return TemplateResponse(ctx, 'acourses/courses_home.html')

def deletar(course_id):
    key = ndb.Key(Course, int(course_id))
    key.delete()
    return RedirectResponse(index)
