# homeapp - views.py
from django.shortcuts import render

#   Index web page view
def index(request):
    return render(request, 'homeapp/home.html')
