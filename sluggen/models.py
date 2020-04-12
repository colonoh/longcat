from django.db import models

class Slug(models.Model):
    created_at = models.DateTimeField('date created', auto_now_add=True)
    url = models.URLField('original version of the URL')
    slug = models.SlugField('shortened version of the URL', max_length=7)
    hits = models.PositiveIntegerField('number of visitors to this slug', default=0)
