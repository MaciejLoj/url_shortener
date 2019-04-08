from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import URLShortener
from .forms import URLForm


class BaseView(View):
    def get(self, request, *args, **kwargs):
        form = URLForm()
        context = {"title": "URL Shortener", "form": form}
        return render(request, "shortenerapp/base_layout.html", context)

    def post(self, request, *args, **kwargs):
        form = URLForm(request.POST)
        context = {"title": "URL Shortener!", "form": form}
        template = "shortenerapp/base_layout.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = URLShortener.objects.get_or_create(url=new_url)
            context = {"object": obj, "created": created}
            if created:
                template = "shortenerapp/url_created.html"
            else:
                template = "shortenerapp/url_exists.html"

        return render(request, template, context)


class URLCbView(View):
    def get(self, request, shorturl=None, *args, **kwargs):
        obj = get_object_or_404(URLShortener, short_url=shorturl)
        return HttpResponseRedirect(obj.url)
