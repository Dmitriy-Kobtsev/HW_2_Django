
from django.core.cache import cache

from config import settings
from .models import Category


def get_category():
    if settings.CACHE_ENABLE:
        key = 'category'
        cache_date = cache.get(key)
        if cache_date is None:
            cache_date = Category.objects.all()
            cache.set(key, cache_date)

        return cache_date

    return Category.objects.all()