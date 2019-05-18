
import webapi.views as views
from rest_framework import routers
from django.conf.urls import url, include

app_name="webapi"

router = routers.DefaultRouter()
router.register(r'district', views.DistrictViewSet)
router.register(r'taluk', views.TalukViewSet)
router.register(r'grampanchayat', views.GramPanchayatViewSet)

urlpatterns=[
    url(r'^/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]