from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os


class Post(models.Model):
    IMG = os.path.join(settings.MEDIA_ROOT, 'img')
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200)
    short_body = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to=IMG, blank=True)

    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.title, self.slug,
                                   self.short_body, self.body)
        
