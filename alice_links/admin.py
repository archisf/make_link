from django.contrib import admin
from alice_links.models import Urls


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_id', 'http_url', 'pub_date', 'count',)
    ordering = ('-pub_date',)
    list_filter = ('name',)

admin.site.register(Urls, UrlsAdmin)
