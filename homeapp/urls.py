# homeapp urls.py
from django.conf.urls import url, include
from . import views

# Route all urls through this view method.
urlpatterns = [
    url(r'^$', views.index, name='index' ),
]