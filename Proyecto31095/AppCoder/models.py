from email.policy import default
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Blog(models.Model):
    name = models.CharField(max_length=40, default=" ")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = RichTextField()
    mini_description = models.TextField(max_length=500, default=" ")
    post_date = models.DateField(default=date.today)
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name + " ==> " + str(self.author)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.post_date))
        return super().save(*args, **kwargs)
