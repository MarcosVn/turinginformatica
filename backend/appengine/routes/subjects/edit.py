# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from course.course_model import Subject, Course
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes import subjects
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

@no_csrf
@login_not_required
def index(subject_id):
    subject = Subject.get_by_id(int(subject_id))
    ctx={'subject': subject,
         'salvar_path': to_path(atualizar)
    }

    ctx["courses"] = Course.query_ordenada_por_nome().fetch()
    return TemplateResponse(ctx, 'subjects/subject_form.html')

@login_not_required
def atualizar(subject_id, name, activities, course):
    subject = Subject.get_by_id(int(subject_id))
    subject.name = name
    subject.activities = activities
    subject.course = ndb.Key(Course, int(course))
    subject.put()
    return RedirectResponse(subjects)