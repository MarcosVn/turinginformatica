# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from subject.subject_model import Subject
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes import subjects
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

@no_csrf
def index(subject_id):
    subject = Subject.get_by_id(int(subject_id))
    ctx={'subject': subject,
         'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx, 'subjects/subject_form.html')

def atualizar(subject_id, name, activities):
    subject = Subject.get_by_id(int(subject_id))
    subject.name = name
    subject.activities = activities
    subject.put()
    return RedirectResponse(subjects)