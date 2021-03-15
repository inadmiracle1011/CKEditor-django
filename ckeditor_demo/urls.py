from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path

from .demo_application.views import ckeditor_form_view

urlpatterns = (
    [
        re_path(r"^$", ckeditor_form_view, name="ckeditor-form"),
        re_path(r"^admin/", admin.site.urls),
        re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
