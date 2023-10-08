from django.db import models
from datetime import datetime, date

class Os_Choice(models.Model):
    os_system = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.os_system
    

# Create your models here.
class Computer(models.Model):
    pc_name = models.CharField(max_length=50, blank=True, null=True) 
    mac_address = models.CharField(max_length=50, blank=False, null=True) 
    ip_address = models.CharField(max_length=50, blank=False, null=True)
    os = models.ManyToManyField(Os_Choice, blank=False)
    username = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=False, null=True)
    update_date = models.DateField("Update Date (mm/dd/yyyy)",auto_now_add=False, auto_now=False, blank=True, null=True)
    purchase_date = models.DateField()
    csv_export = models.BooleanField(blank=False, null=True)

    def __str__(self):
        return self.os
    
   
class ComputerHistory(models.Model):
     pc_name = models.CharField(max_length=30, blank=True, null=True)
     ip_address = models.CharField(max_length=30, blank=True, null=True)
     mac_address = models.CharField(max_length=30, blank=True, null=True)
     username = models.CharField(max_length=30, blank=True, null=True)
     location = models.CharField(max_length=30, blank=True, null=True)
     update_date = models.DateField("Update Date (mm/dd/yyyy)",auto_now_add=False, auto_now=False, blank=True, null=True)
     purchase_date = models.DateField()

     def __str__(self):
        return self.pc_name