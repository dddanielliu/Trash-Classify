import os
from django.db import models

class HisDataQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for obj in self:
            if obj.image:
                # Delete the file from storage
                if os.path.isfile(obj.image.path):
                    os.remove(obj.image.path)
        super(HisDataQuerySet, self).delete(*args, **kwargs)