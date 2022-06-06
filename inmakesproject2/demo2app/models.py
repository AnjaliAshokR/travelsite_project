from django.db import models

# Create your models here.
class places(models.Model):
    place_name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()

    def __str__(self):
        return  self.place_name
class travel_agents(models.Model):
    name=models.CharField(max_length=250)
    imag=models.ImageField(upload_to='photos')
    descr=models.TextField()

    def __str__(self):
        return  self.name