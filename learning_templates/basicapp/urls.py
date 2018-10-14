from django.conf.urls import url
from django.urls import path
from . import views
# TEMPLATES TAGGING
app_name = 'basicapp'

urlpatterns = [
     path('relative/', views.relative, name='relative'),
     path('other/', views.other, name='other'),
]
