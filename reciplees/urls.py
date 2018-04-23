from django.conf.urls import include, url
from django.http import HttpResponseRedirect
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^recipes/', include('recipes.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('recipes/')),
]