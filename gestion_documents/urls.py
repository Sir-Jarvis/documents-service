from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('documents.endPoints')),
    path('schema/', get_schema_view(
        title="DocumentsAPI",
        description="API pour gestion des documents",
        version="1.0.0"
    ), name="documents-schema"),
    path('', include_docs_urls(
        title="DocumentAPI",
        description="API pour gestion des documents",
    ), name="documents-docs")
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
