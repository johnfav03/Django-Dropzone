from django.db import models

class Drop(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.pk)