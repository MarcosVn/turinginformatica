# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from user.user_model import User
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.users import edit
from routes.users.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

__author__ = 'marcos'

@no_csrf
@login_not_required
def index():
    query = User.query_ordenada_por_criacao()
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)
    user = query.fetch()
    if len(user) >= 1:
        user = user[len(user)-1]
        key = user.key
        key_id = key.id()
        user.edit_path = to_path(edit_path_base, key_id)
        user.deletar_path = to_path(deletar_path_base, key_id)


    ctx = {'user': user,
           'salvar_path': to_path(salvar)}

    return TemplateResponse(ctx, 'users/user_home.html')

@login_not_required
def deletar(user_id):
    key = ndb.Key(User, int(user_id))
    key.delete()
    return RedirectResponse(index)
