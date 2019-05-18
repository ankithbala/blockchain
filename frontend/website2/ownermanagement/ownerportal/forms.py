from django.forms import forms, fields


class SetOwnerForm(forms.Form):
    land_number=fields.CharField()
    owner_name=fields.CharField()
    aadhar_number=fields.CharField()
    pan_number=fields.CharField()

class SellLandForm(forms.Form):
    from_aadhar=fields.CharField()
    land_number=fields.CharField()
    owner_name=fields.CharField()
    aadhar_number=fields.CharField()
    pan_number=fields.CharField()