from operator import attrgetter

from django import template
from django.db.models import Count

from women.models import *

register = template.Library()

# @register.simple_tag(name='get_cats')
# def get_categories(filter=None):
#     if not filter:
#         # return Category.objects.all()
#         womens = Women.objects.filter(is_published=True)
#         cats = []
#         for i in womens:
#             if i.cat not in cats:
#                 cats.append(i.cat)
#         return cats
#     else:
#         return Category.objects.filter(pk=filter)

# @register.inclusion_tag('women/list_categories.html')
# def show_categories(sort=None, cat_selected=0):
#     if not sort:
#         # cats = Category.objects.all()
#         womens = Women.objects.filter(is_published=True)
#         cats = []
#         for i in womens:
#             if i.cat not in cats:
#                 cats.append(i.cat)
#
#     else:
#         # cats = []
#         # allCats = Category.objects.all()
#         # for cat in allCats:
#         #     if cat.women_set.exists():
#         #         cats.append(cat)
#
#         # cats = []
#         # category = Category
#
#         cats = Category.objects.annotate(total=Count('women')).filter(total__gt=0)
#
#     return {'cats': cats, 'cat_selected': cat_selected}