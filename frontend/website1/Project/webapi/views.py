from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from webapi.serializers import DistrictSerializer, TalukSerializer,\
    GramPanchayatSerializer
from baseportal.models import District, Taluk, GramPanchayat

# Create your views here.

class DistrictViewSet(ReadOnlyModelViewSet):
    queryset=District.objects.all()
    serializer_class=DistrictSerializer


class TalukViewSet(ReadOnlyModelViewSet):
    queryset=Taluk.objects.all()
    serializer_class=TalukSerializer
    filter_fields=('district',)


class GramPanchayatViewSet(ReadOnlyModelViewSet):
    queryset=GramPanchayat.objects.all()
    serializer_class=GramPanchayatSerializer
    filter_fields=('taluk',)
    