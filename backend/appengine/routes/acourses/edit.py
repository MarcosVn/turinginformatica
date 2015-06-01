# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from course.course_model import Course, Subject
from gaepermission.decorator import login_not_required
from routes import acourses
from gaecookie.decorator import no_csrf
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

@no_csrf
@login_not_required
def index(course_id):
    course = Course.get_by_id(int(course_id))
    ctx = {'course': course,
           'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx, 'acourses/courses_form.html')


@login_not_required
def atualizar(course_id, name, duration, educationProject):
    course = Course.get_by_id(int(course_id))
    course.name = name
    course.duration = duration
    course.educationProject = educationProject
    course.put()
    return RedirectResponse(acourses)

