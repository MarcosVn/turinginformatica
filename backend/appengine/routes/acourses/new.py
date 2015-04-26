# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from course.course_model import Course, CourseForm, Subject
from config.template_middleware import TemplateResponse
from routes import acourses
from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'marcos'

def salvar(**kwargs):
    kwargs['subjects'] = ndb.Key(Subject, int(kwargs['subjects']))
    form = CourseForm(**kwargs)
    # erros = form.validate()
    # if erros:
    #     return

    # course.put()
    # kwargs = form.normalize()

    course = form.fill_model()
    course = Course(**kwargs)
    course.put()
        # return RedirectResponse(acourses)

    # else:
    #     ctx = {'courses': kwargs, 'erros': erros}
    return RedirectResponse(acourses)