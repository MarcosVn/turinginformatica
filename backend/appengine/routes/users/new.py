# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaepermission.decorator import login_not_required
from user.user_model import User, UserForm
from config.template_middleware import TemplateResponse
from routes import users
from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'marcos'


@login_not_required
def salvar(**kwargs):
    form = UserForm(**kwargs)
    erros = form.validate()
    if not erros:
        properties = form.normalize()
        user = User(**properties)
        user.put()
        return RedirectResponse(users)

    else:
        ctx = {'users': kwargs, 'erros': erros}
        return TemplateResponse(ctx, 'users/user_home.html')