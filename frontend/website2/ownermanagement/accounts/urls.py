from django.urls.conf import path
from django.conf.urls import include


app_name="accounts"

urlpatterns=[
    path('',include("django.contrib.auth.urls")),
]
