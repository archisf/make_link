# -*- coding: utf-8 -*-
import random
import string

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from alice_links.forms import UrlsForm
from alice_links.models import Urls


def redirect_original(request, short_id):
    url = get_object_or_404(Urls, pk=short_id)
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.http_url)


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        return short_id


@login_required()
def add_shorten_url(request):
    if request.method == 'POST':
        form = UrlsForm(request.POST)
        if form.is_valid():
            b = form.cleaned_data
            url = b['http_url']
            short_id = get_short_code()
            first_name = b['name']
            b = Urls(http_url=url, short_id=short_id, name=first_name)
            b.save()
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')


@login_required()
def latest_urls(request):
    urls_list = Urls.objects.order_by('-pub_date')[:5]
    return render(request, 'alice_links/index.html', {'urls_list': urls_list})
