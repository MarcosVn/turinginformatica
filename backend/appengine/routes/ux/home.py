from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.login import google
from tekton import router

__author__ = 'Marcos'

@login_not_required
@no_csrf
def index(ret_path='/'):
    g_path = router.to_path(google.index, ret_path=ret_path)
    return TemplateResponse()