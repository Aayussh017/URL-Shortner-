from django.shortcuts import render, redirect
from django.http import Http404
from django.views import View
from .models import ShortURL
from django.utils.crypto import get_random_string
from django.db.models import Count

def home(request):
    short_url = None
    total_short_urls = ShortURL.objects.count()
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_url_instance = ShortURL(original_url=original_url)
        short_url_instance.save()
        short_url = request.build_absolute_uri(f'/{short_url_instance.short_url}/')
    return render(request, 'home.html', {'short_url': short_url, 'total_short_urls': total_short_urls})

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_url_instance = ShortURL(original_url=original_url)
        short_url_instance.save()
        short_url = request.build_absolute_uri(f'/{short_url_instance.short_url}/')
        return render(request, 'home.html', {'short_url': short_url})
    return redirect('home')

class RedirectShortURL(View):
    def get(self, request, short_url):
        try:
            short_url_obj = ShortURL.objects.get(short_url=short_url)
        except ShortURL.DoesNotExist:
            raise Http404("Short URL does not exist")
        return redirect(short_url_obj.original_url)

def list_short_urls(request):
    short_urls = ShortURL.objects.all()
    total_short_urls = short_urls.count()
    return render(request, 'urlshort/list_short_urls.html', {'short_urls': short_urls, 'total_short_urls': total_short_urls})