# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from course.course_model import Subject, Course
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions, login_not_required
from permission_app.model import ADMIN
from routes.subjects import edit
from routes.subjects.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

# @permissions(ADMIN)
@no_csrf
@login_not_required
def index(course_selecionado=None):
    # query = Subject.query_ordenada_por_nome().fetch()
    # edit_path_base = to_path(edit)
    # deletar_path_base = to_path(deletar)
    # subjects = query
    # for s in subjects:
    #     key = s.key
    #     key_id = key.id()
    #     s.edit_path = to_path(edit_path_base, key_id)
    #     s.deletar_path = to_path(deletar_path_base, key_id)
    # ctx = {'salvar_path': to_path(salvar),
    #        'subjects': subjects}
    #
    # return TemplateResponse(ctx, 'subjects/subject_home.html')

    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)
    ctx = {'courses': Course.query_ordenada_por_nome().fetch(),
           'salvar_path': to_path(salvar)}

    if course_selecionado is None:
        ctx['subjects'] = Subject.query_ordenada_por_nome().fetch()
        ctx['course_selecionado'] = None


    else:
        ctx['course_selecionado'] = Course.get_by_id(int(course_selecionado))
        ctx['subjects']= Subject.query_ordenada_por_courses(course_selecionado).fetch()


    for subject in ctx['subjects']:
        key = subject.key
        key_id = key.id()
        subject.edit_path = to_path(edit_path_base, key_id)
        subject.deletar_path = to_path(deletar_path_base, key_id)


    return TemplateResponse(ctx, 'subjects/subject_home.html')



@login_not_required
def deletar(subject_id):
    key = ndb.Key(Subject, int(subject_id))
    key.delete()
    return RedirectResponse(index)
