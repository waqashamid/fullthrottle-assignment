from django.conf.urls import url
from .api import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^(?P<word>[\w.-]+)$', SearchWords.as_view(), name='upload_file'),
]
