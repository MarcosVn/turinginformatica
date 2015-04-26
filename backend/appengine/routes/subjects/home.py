# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from course.course_model import Subject
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import ADMIN
from routes.subjects import edit
from routes.subjects.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

# @permissions(ADMIN)
@no_csrf
def index():
    query = Subject.query_ordenada_por_nome()
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)
    subjects = query.fetch()
    for s in subjects:
        key = s.key
        key_id = key.id()
        s.edit_path = to_path(edit_path_base, key_id)
        s.deletar_path = to_path(deletar_path_base, key_id)
    ctx = {'salvar_path': to_path(salvar),
           'subjects': subjects}

    return TemplateResponse(ctx, 'subjects/subject_home.html')

def deletar(subject_id):
    key = ndb.Key(Subject, int(subject_id))
    key.delete()
    return RedirectResponse(index)
