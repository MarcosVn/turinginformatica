# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from course.course_model import Course
from routes import acourses
from gaecookie.decorator import no_csrf
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

@no_csrf
def index(course_id):
    course = Course.get_by_id(int(course_id))
    ctx = {'course': course,
           'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx, 'acourses/courses_form.html')

def atualizar(course_id, name, duration, subjects):
    course = Course.get_by_id(int(course_id))
    course.name = name
    course.duration = (int(duration))
    course.subjects = subjects
    course.put()
    return RedirectResponse(acourses)

