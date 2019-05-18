from rest_framework import serializers
from baseportal.models import District, GramPanchayat, Taluk




class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields=('id','name')


class TalukSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taluk
        fields=('id','name','district')


class GramPanchayatSerializer(serializers.ModelSerializer):
    class Meta:
        model=GramPanchayat
        fields=('id','name','taluk')