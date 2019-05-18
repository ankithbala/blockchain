from django.forms import forms
from django import forms
from baseportal.models import District, Taluk, GramPanchayat
from django.forms.utils import ErrorList

class LandForm(forms.Form):
    district=forms.ModelChoiceField(queryset=District.objects.all(), 
                                    widget=forms.Select(attrs={"onChange":"getDistrict(this.value)"})
                                    )
    taluk=forms.ModelChoiceField(queryset=Taluk.objects.all(),
                                 widget=forms.Select(attrs={"onChange":"getTaluk(this.value)"})
                                )
    gram_panchayat=forms.ModelChoiceField(queryset=GramPanchayat.objects.all())
    land_number=forms.CharField()
    