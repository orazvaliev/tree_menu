from django import template
from menu.models import MenuItem
from django.urls import reverse


register = template.Library()


@register.inclusion_tag('test.html', takes_context=True)
def show_tree_items(context):
    request = context['request']

    if request.path == '/':
        items_tree = MenuItem.objects.filter(parent=None)

    else:
        current_slug = request.path.split('/')[-2]
        obj = MenuItem.objects.get(slug=current_slug)
        items_tree = MenuItem.objects.\
            filter(right__gt=obj.left).\
            filter(left__lt=obj.right).\
            exclude(level__gt=obj.level+1)

    for item in items_tree:
        item.absolute_url = reverse('menu:' + str(item.slug))

    return {'items_tree': items_tree}

