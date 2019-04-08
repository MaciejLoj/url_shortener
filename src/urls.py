
from django.conf.urls import url
from django.contrib import admin

from shortenerapp.views import URLCbView, BaseView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BaseView.as_view()),
    url(r'^(?P<shorturl>[\w-]+)/$', URLCbView.as_view()),
]
