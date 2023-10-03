from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['pc_name','mac_address','ip_address','unit','location','added_by','created_at','updated_by','updated_at']

    