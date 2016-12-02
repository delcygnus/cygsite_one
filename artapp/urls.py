# artapp - urls.py - delcygnus
from django.conf.urls import url
from . import views

# Route artapp urls through this view method
urlpatterns = [
    url(r'^', views.artapp, name='artapp' ),
]