from django.db import models
import os
import requests
from django.core.files.storage import FileSystemStorage
from django.conf import settings

upload_storage = FileSystemStorage(location=settings.UPLOAD_ROOT)
# Create your models here.
class HisData(models.Model):
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    image = models.ImageField(upload_to='images', storage=upload_storage) 
    label = models.IntegerField(null=True, blank=True)
    label_name = models.CharField(max_length=255, null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)


    def delete(self, *args, **kwargs):
        # Delete the image file before deleting the model instance
        if self.image:
            # Delete the file from storage
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        # Call the original delete method to delete the model instance from the database
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(HisData, self).save(*args, **kwargs)
        if self.image and self.label is None:
            if os.path.isfile(self.image.path):
                result_json={}
                url = "http://model:8188/predict/"
                response = requests.get(url+"?img_path={}".format(os.path.abspath(self.image.path)))

                if response.status_code == 200:
                    result_json = response.json()  # or response.text depending on your API response
                    self.label = result_json['label']
                    self.label_name = result_json['label_name']
                super(HisData, self).save(*args, **kwargs)


    # add_date.editable = True