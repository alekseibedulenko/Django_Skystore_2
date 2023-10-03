from django.db import models
from pytils.translit import slugify


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.SlugField(max_length=100, verbose_name='slug', unique=True)
    description = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение')
    issued_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(args, **kwargs)







