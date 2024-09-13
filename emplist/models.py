from django.db import models

# Create your models here.
class Emp(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.code