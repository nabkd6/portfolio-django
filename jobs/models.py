from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, default=None)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
