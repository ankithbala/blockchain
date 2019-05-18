from django.db import models

# Create your models here.

class District(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Taluk(models.Model):
    name=models.CharField(max_length=50)
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class GramPanchayat(models.Model):
    name=models.CharField(max_length=50)
    taluk=models.ForeignKey(Taluk, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


