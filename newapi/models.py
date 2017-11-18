from django.db import models

class TextUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ('created',)
