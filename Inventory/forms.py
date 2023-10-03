from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['pc_name','mac_address','ip_address','os','username','location']

class SearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['pc_name', 'username']

    def clean_item_name(self):
        item_name = self.cleaned_data.get('pc_name')

        if Computer.objects.filter(item_name=item_name).exists():
            raise forms.ValidationError('An item with this name already exists.')

        return item_name     