from django.db import models

# Create your models here.
class Computer(models.Model):
    pc_name = models.CharField(max_length=50, blank=True, null=True) 
    mac_address = models.CharField(max_length=50, blank=True, null=True) 
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    os = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.pc_name
