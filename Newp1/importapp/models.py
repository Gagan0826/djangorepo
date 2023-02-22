from django.db import models
import math
class Alumni(models.Model):
    usn=models.CharField(max_length=10,null=True,blank=True)
    name=models.CharField(max_length=20)
    batch=models.IntegerField(default=0)
    company=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=50,null=True)
    PROEmail=models.CharField(max_length=20,null=True)
    OFFEmail=models.CharField(max_length=20,null=True)
    contact_no=models.CharField(max_length=12)
    designation=models.CharField(max_length=20,null=True)
    domain=models.CharField(max_length=15,null=True)
    willing_contribution=models.CharField(max_length=20,null=True)

    def save(self, *args, **kwargs):
        if self.batch is not None and not math.isnan(self.batch):
            self.batch = int(self.batch)
        super(Alumni, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
