from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['pc_name','mac_address','ip_address','os','username','location', 'purchase_date']

class SearchForm(forms.ModelForm):
    #csv_export = forms.BooleanField(required = False)
    class Meta:
        model = Computer
        fields = ['pc_name', 'username']# 'csv_export']