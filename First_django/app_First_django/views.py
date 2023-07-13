from django.shortcuts import render


def index(reqest):
    return render(reqest, 'index.html')

def top(reqest):
    return render(reqest, 'top-sellers.html')


