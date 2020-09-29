from django.db import models

# Create your models here.
class MangaEntry(models.Model):
    name = models.CharField(max_length=200,default='Placeholder')
    current_chapter = models.IntegerField(default=0)
    last_read = models.DateTimeField('Last read date')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

