from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('sort', srt, name='sort'),
    path('update', update, name='update'),
    path('delete', delete, name='delete')
 
]
