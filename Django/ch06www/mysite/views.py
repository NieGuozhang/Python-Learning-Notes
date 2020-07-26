from django.shortcuts import render
from datetime import datetime


# Create your views here.

def index(request, tvno=0):
    # msg = 'Hello'
    now = datetime.now()
    return render(request, 'index.html', locals())
