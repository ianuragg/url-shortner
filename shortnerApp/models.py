from django.db import models

#Election
class Shortner(models.Model):
    url = models.CharField(max_length=1000, verbose_name="Website URL")
    slug = models.CharField(max_length=15, verbose_name="Short Link", unique=True)
    date_created = models.DateTimeField(verbose_name="date created", auto_now_add=True)  
    is_active = models.BooleanField()

    def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"