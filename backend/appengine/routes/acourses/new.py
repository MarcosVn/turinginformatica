# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from course.course_model import Course, CourseForm
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required
from routes import acourses
from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'marcos'


@login_not_required
def salvar(**kwargs):
    form = CourseForm(**kwargs)
    erros = form.validate()
    if not erros:
        properties = form.normalize()
        course = Course(**properties)
        course.put()
        return RedirectResponse(acourses)

    else:
        ctx = {'courses': kwargs, 'erros': erros}
        return TemplateResponse(ctx, 'acourses/courses_home.html')


