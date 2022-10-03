from email.policy import default
from django.db import models
from django.forms import CharField, IntegerField
from UserCoder.models import User
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=40, default=" ")
    subtitle = models.TextField(max_length=500, default=" ")
    author = models.CharField(max_length=40, default=" ")
    description = RichTextField()
    post_date = models.DateField(default=date.today)
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title + " ==> " + str(self.author)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + str(self.post_date))
        return super().save(*args, **kwargs)
