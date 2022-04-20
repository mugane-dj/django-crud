from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        labels = {
            'material_code': 'Material Code',
            'material_description': 'Material Description',
            'order_quantity': 'Order Quantity',
            'material_type': 'Material Type',
            'location': 'Location',
            'quantity_issued': 'Quantity Issued'
        }
    def __init__(self, *args, **kwargs):
        super(InventoryForm, self).__init__(*args, **kwargs)
        self.fields['material_type'].empty_label = "Select"
        self.fields['location'].empty_label = "Select"