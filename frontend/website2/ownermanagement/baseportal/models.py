from django.db import models

# Create your models here.
class PublicKey(models.Model):
    aadhar=models.IntegerField()
    p_val=models.IntegerField()
    q_val=models.IntegerField()
    def n_val(self):
        return self.p_val*self.q_val