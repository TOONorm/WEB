from django.shortcuts import render
from .models import Advert

def index(reqest):
    advert = Advert.objects.all()
    context = {'advertisment': advert}
    return render(reqest, 'index.html', context)

def top(reqest):
    return render(reqest, 'top-sellers.html')


