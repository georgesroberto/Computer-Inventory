from django.db import models

# Create your models here.
class Computer(models.Model):
    pc_name = models.CharField(max_length=50, blank=True, null=True) 
    mac_address = models.IntegerField(blank=True, null=True) 
    ip_address = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    added_by = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.pc_name
