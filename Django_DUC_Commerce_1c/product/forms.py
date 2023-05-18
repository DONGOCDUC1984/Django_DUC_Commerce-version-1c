from django import forms
from .models import Product
INPUT_CLASSES = 'py-1'

class NewProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = ("category","name","description","price","image","tel","province_city")
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            "tel": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            "province_city": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
class EditProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = ("category","name","description","price","image","is_sold","tel","province_city")
        
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
             "tel": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            "province_city": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            
        } 
               