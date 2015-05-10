# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from course.course_model import Subject, SubjectForm
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required
from routes import subjects
from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'marcos'

@login_not_required
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