from django.contrib import admin

# Register your models here.

import csv
from django.http import HttpResponse
from .models import SalesData  # Replace with your actual model name
from .etl import process_csv  # Your custom function to handle CSV processing


# Define the admin action to upload CSV
def upload_csv(modeladmin, request, queryset):
    # This will handle the CSV upload logic
    from django import forms
    from django.shortcuts import render
    import csv

    class UploadCsvForm(forms.Form):
        file = forms.FileField()

    if request.method == "POST":
        form = UploadCsvForm(request.POST, request.FILES)
        if form.is_valid():
            # Process CSV file
            csv_file = form.cleaned_data["file"]
            csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
            next(csv_data)  # Skip header row if present
            # Process each row in the CSV file
            for row in csv_data:
                process_csv(row)  # Call your custom ETL function to handle each row
            return HttpResponse("CSV file uploaded and processed successfully!")
    else:
        form = UploadCsvForm()

    return render(
        request,
        "admin/csv_upload.html",  # Create a template to upload the CSV file
        {"form": form},
    )


# Register the admin action and add it to your model admin
class SalesDataAdmin(admin.ModelAdmin):
    actions = [upload_csv]

admin.site.register(SalesData, SalesDataAdmin)
