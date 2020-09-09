from django.db import models

class Resources(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    software = models.CharField(max_length=200)
    notes = models.CharField(max_length=500)
    image = models.FileField(upload_to='uploads/')

    def __str__(self):
        return [self.id, self.title, self.url, self.software, self.notes]
