from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse
from services.models import Service


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            'root:home',
            'root:about',
            'root:contact',
            'services:services',

        ]
    def location(self, item):
        return reverse(item)

class DynamicViewSitemap(Sitemap):
    priority = 0.5
    changefreg = "daily"

    def items(self):
        return Service.objects.all()
    
    def location(self, obj):
        return '/services/service-detail/%i'%obj.id
    