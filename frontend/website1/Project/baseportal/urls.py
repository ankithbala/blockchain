from django.urls.conf import path
from baseportal.views import HomePageView, LandRecordView

app_name='baseportal'

urlpatterns=[
    path('', HomePageView.as_view(), name='homepage'),
    path('landrecord', LandRecordView.as_view(), name='landrecord')
]