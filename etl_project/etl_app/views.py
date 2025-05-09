# views.py
from django.shortcuts import render

def test_view(request):
    return render(request, "admin/csv_upload.html")
