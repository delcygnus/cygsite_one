# statementapp - urls.py - delcygnus
from django.conf.urls import url
from . import views

# Route statementapp urls through this view method
urlpatterns = [
    url(r'^', views.statementapp, name='statementapp' ),
]
