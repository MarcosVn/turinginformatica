
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from gaecookie.decorator import no_csrf
from gaepermission import facade
from gaepermission.decorator import login_not_required
from tekton import router
from config.template_middleware import TemplateResponse
from routes.login import google, facebook
from routes.login.passwordless import send_email

__author__ = 'Marcos'



@login_not_required
@no_csrf
def index(ret_path='/'):
    g_path = router.to_path(google.index, ret_path=ret_path)
    return TemplateResponse()