from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    # display = forms.ImageField()
    class Meta:
        model = Product
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if(visible.name!="display"):
                visible.field.widget.attrs['class'] = 'form-control'


