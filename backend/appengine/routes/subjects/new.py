# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from subject.subject_model import Subject, SubjectForm
from config.template_middleware import TemplateResponse
from routes import subjects
from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'marcos'

def salvar(**kwargs):
    form = SubjectForm(**kwargs)
    erros = form.validate()
    if not erros:
        properties = form.normalize()
        subject = Subject(**properties)
        subject.put()
        return RedirectResponse(subjects)

    else:
        ctx = {'subjects': kwargs, 'erros': erros}
        return TemplateResponse(ctx, 'subjects/subject_form.html')