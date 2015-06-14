# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from config.template_middleware import TemplateResponse
from mock import Mock
from routes.acourses import new
from course.course_model import Course
from routes.acourses import rest
from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'marcos'


class NewTest(GAETestCase):
    def test_sucess(self):
        resposta = new.salvar(name='Análise e Desenvolvimento de Sistemas',
                              duration='6 semestres',
                              educationProject='Plano de ensino X')
        self.assertIsInstance(resposta, RedirectResponse)
        self.assertEqual('/acourses', resposta.context)
        courses = Course.query().fetch()
        self.assertEqual(1, len(courses))
        course = courses[0]
        self.assertEqual('Análise e Desenvolvimento de Sistemas', course.name)
        self.assertEqual('6 semestres', course.duration)
        self.assertEqual('Plano de ensino X', course.educationProject)

    def test_validation(self):
        resposta = new.salvar()
        self.assertIsInstance(resposta, TemplateResponse)
        self.assert_can_render(resposta)
        self.assertIsNone(Course.query().get())
        self.maxDiff = None
        self.assertDictEqual({u'courses': {},
                              u'erros': {'name': u'Required field',
                                         'duration': u'Required field',
                                         'educationProject': u'Required field'}}
                             , resposta.context)


    def test_json_error(self):
        respota_mock=Mock()
        resposta = rest.salvar(respota_mock)
        respota_mock.set_status.assert_called_once_with(400)
        self.assert_can_serialize_as_json(resposta)