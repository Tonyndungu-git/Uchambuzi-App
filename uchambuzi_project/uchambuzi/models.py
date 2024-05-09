from django.db import models

# Create your models here.

class UploadedData(models.Model):
    # Metadata for the uploaded file
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"Uploaded Data - {self.upload_date}"
