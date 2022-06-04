from django.urls import URLPattern, path
from.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
]