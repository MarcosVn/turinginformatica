from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from config.template_middleware import TemplateResponse

__author__ = 'Marcos'

@no_csrf
def index():
    return TemplateResponse()



