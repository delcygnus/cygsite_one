# cygsite - urls.py - delcygnus
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^art---', include('artapp.urls')),
    url(r'^notes/', include('notesapp.urls')),
    url(r'^', include('homeapp.urls')),
]
