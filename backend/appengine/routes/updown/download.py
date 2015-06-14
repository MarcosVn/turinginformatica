# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes import updown
from tekton.gae.middleware.redirect import RedirectResponse

__author__ = 'marcos'


@no_csrf
@login_not_required

def index(_handler, blob_key, filename):
    _handler.send_blob(blob_key)

