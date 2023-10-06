from django import forms
from .models import *

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['pc_name','mac_address','ip_address','os','username','location', 'purchase_date']

    def clean_pc_name(self): 
        pc_name = self.cleaned_data.get('pc_name')
        if (pc_name == ""):
            raise forms.ValidationError('Oops please fill pc_name')
        for instance in Computer.objects.all():
            if instance.pc_name == pc_name:
                raise forms.ValidationError('pc_name already exists' )
        return pc_name
    
    def clean_ip_address(self): 
        ip_address = self.cleaned_data.get('ip_address')
        if (ip_address == ""):
            raise forms.ValidationError('Oops please fill ip_address')
        for instance in Computer.objects.all():
            if instance.ip_address == ip_address:
                raise forms.ValidationError(' IP_address already exist' )
        return ip_address
    
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['pc_name','mac_address','os','username','location', 'update_date']

class SearchForm(forms.ModelForm):
    csv_export = forms.BooleanField(required = False)
    class Meta:
        model = Computer
        fields = ['pc_name', 'username', 'csv_export']

class AddOsForm(forms.ModelForm):
    class Meta:
        model = Os_Choice
        fields = ['os_system']