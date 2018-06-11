from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Menu(models.Model):
    menu_name = models.CharField(max_length=25)

    def __str__(self):
        return self.menu_name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu,
                             blank=False,
                             related_name='item',
                             on_delete=models.CASCADE)
    left = models.IntegerField(blank=True,
                               null=True)
    right = models.IntegerField(blank=True,
                                null=True)
    parent = models.ForeignKey('self',
                               blank=True,
                               null=True,
                               related_name='children',
                               on_delete=models.CASCADE)
    position = models.IntegerField(blank=True,
                                   null=True)
    level = models.IntegerField(blank=True,
                                null=True)
    title = models.CharField(max_length=25,
                             unique=True)
    slug = models.SlugField(max_length=30,
                            unique=True)

    def __str__(self):
        level = self.level if self.level else 1
        i = '| ' if level > 1 else ''
        return ('|--' * (level - 1)) + i + self.title

    class Meta:
        ordering = ('left', )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        self.set_mptt()


    def set_mptt(self, left=1, parent=None, level=1):
        for i in type(self).objects.filter(parent=parent).order_by('position'):
            obj = i
            children_count = 0

            while obj.children.exists():
                for child in obj.children.all():
                    children_count += 1
                    obj = child

            data = {
                'level': level,
                'left': left,
                'right': left + (children_count * 2) + 1
            }
            type(self).objects.filter(id=i.id).update(**data)
            left = data['right'] + 1
            self.set_mptt(left=data['left'] + 1, parent=i.id, level=data['level'] + 1)