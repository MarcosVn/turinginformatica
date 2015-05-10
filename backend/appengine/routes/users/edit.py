# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required
from user.user_model import User
from routes import users
from gaecookie.decorator import no_csrf
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

@no_csrf
@login_not_required
def index(user_id):
    user = User.get_by_id(int(user_id))
    ctx = {'user': user,
           'salvar_path': to_path(atualizar)}
    return TemplateResponse(ctx, 'users/user_form.html')

@login_not_required
def atualizar(user_id, uusername, upassword, uemail, uname, ubirthday):
    user = User.get_by_id(int(user_id))
    user.uusername = uusername
    user.upassword = upassword
    user.uemail = uemail
    user.uname = uname
    user.ubirthday = ubirthday
    user.put()
    return RedirectResponse(users)

