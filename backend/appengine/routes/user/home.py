from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from config.template_middleware import TemplateResponse
from tekton import router

__author__ = 'marcos'

@login_not_required
@no_csrf
def index():
    return TemplateResponse()


def save(_resp, **properties):
    _resp.write(properties)