from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Menu(models.Model):
    menu_name = models.CharField(max_length=25)

    def __str__(self):
        return self.menu_name

    def get_menu_tree(self):
        objects = self.objects.get(menu_name=self.menu_name).items.all()
        print(objects)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu,
                             blank=False,
                             related_name='items',
                             on_delete=models.CASCADE)

    parent = models.ForeignKey('self',
                               blank=True,
                               null=True,
                               related_name='children',
                               on_delete=models.CASCADE)

    name = models.CharField(max_length=25,
                            unique=True)
    slug = models.SlugField(primary_key=True,
                            max_length=30,
                            unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('menu', kwargs={'slug': self.slug})
