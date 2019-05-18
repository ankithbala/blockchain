from django.urls.conf import path
from ownerportal.views import SetOwnerView, SellLandView, HomePageView


app_name="ownerportal"

urlpatterns=[
    path('setowner/', SetOwnerView.as_view(), name="setowner"),
    path('sellitem/', SellLandView.as_view(), name="sellland"),
    path('', HomePageView.as_view(), name="homepage"),
]