# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging

from google.appengine.api.app_identity import get_default_gcs_bucket_name
from google.appengine.ext.blobstore import blobstore

from blob_app import blob_facade
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from routes.updown import upload
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from routes.updown import download

__author__ = 'marcos'


@no_csrf
@login_required
def index(_logged_user):
    success_url = router.to_path(upload)
    bucket = get_default_gcs_bucket_name()
    logging.info(bucket)
    url = blobstore.create_upload_url(success_url, gs_bucket_name=bucket)
    cmd = blob_facade.list_blob_files_cmd(_logged_user)
    blob_form = blob_facade.blob_file_form()
    deletar_path_base = router.to_path(delete)
    download_path_base = router.to_path(download)


    def localizar_blob(blob):
        dct = blob_form.fill_with_model(blob)
        dct["delete_path"] = router.to_path(deletar_path_base, dct["id"])
        dct["download_path"] = router.to_path(download_path_base, blob.blob_key, dct["filename"].encode("utf8"))

        return dct

    blob_files = [localizar_blob(b) for b in cmd()]

    ctx = {'upload_url': url,
           'blob_files': blob_files}

    return TemplateResponse(ctx, 'updown/home.html')


@no_csrf
@login_required
def delete(blob_key):
    blob_facade.delete_blob_file_cmd(blob_key).execute()
    return RedirectResponse(index)