# etl_app/urls.py

from django.urls import path
from .views import upload_csv_view

urlpatterns = [
    path('test-upload/', upload_csv_view, name='test-upload'),  # Test URL for csv_upload.html
]
