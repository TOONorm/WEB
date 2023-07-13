from django.urls import path
from .views import index, top


urlpatterns = [
    path('',index, name="main-page"),
    path('top-sellers/', top, name='top-sellers')
]