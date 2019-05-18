from django.contrib import admin
from baseportal.models import District, GramPanchayat, Taluk

# Register your models here.
admin.site.register(District)
admin.site.register(Taluk)
admin.site.register(GramPanchayat)