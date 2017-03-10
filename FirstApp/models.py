from django.db import models

# Create your models here.
class Pri(models.Model):
    Pcol1 = models.CharField(max_length=50)
    Pcol2 = models.CharField(max_length=10)
    Pcol3 = models.CharField(max_length=20)
    def __str__(self):
        return self.Pcol1 + ' ---- ' + self.Pcol2
    def get_absolute_url(self):
        return "/FirstApp"

class Sec(models.Model):

    Scol1 = models.ForeignKey(Pri, on_delete=models.CASCADE)
    Scol2 = models.CharField(max_length=30)
    Scol3 = models.CharField(max_length=10)
