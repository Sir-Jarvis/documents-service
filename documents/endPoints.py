from django.urls import path, include
from documents import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.DocumentAPIView.as_view()),
    path('uploadFile/',views.FileUploadView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
