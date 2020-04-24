from django.db import models

class Slug(models.Model):
    created_at = models.DateTimeField('date created', auto_now_add=True)
    url = models.URLField('original version of the URL')
    slug = models.SlugField('shortened version of the URL', max_length=7, primary_key=True)
    hits = models.PositiveIntegerField('number of visitors to this slug', default=0)

    def __str__(self):
        return f'{self.slug} -> {self.url}'