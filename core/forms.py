from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    # unit= forms.CharField(
    #     widget=forms.Select(choices=[('INCHES', 'inches'),('CM', 'cm'),('MM', 'mm')]),
    # )
    class Meta:
        model = Inquiry
        fields = [
            'length',
            'width',
            'height',
            'unit',
            'quantity',
            'printing',
            'stock',
            'art_work',
            'full_name',
            'email',
            'phone',
            'notes'
        ]

    def __init__(self, *args, **kwargs):
        super(InquiryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if(visible.name!='art_work'):
                visible.field.widget.attrs['class'] = 'form-control'

