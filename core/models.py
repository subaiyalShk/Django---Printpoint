from django.db import models
from catalogue.models import Product
from django.core.validators import MinValueValidator


class Inquiry(models.Model):
    length=models.IntegerField()
    width=models.IntegerField()
    height=models.IntegerField()
    unit=models.CharField(max_length=45, choices=[(None, 'Select'), ('INCHES', 'inches'), ('CM', 'cm'), ('MM', 'mm')])
    quantity=models.IntegerField()
    printing=models.CharField(max_length=45, choices=[(None, 'Select'), ('YES', 'Yes'), ('NO', 'No')])
    stock=models.CharField(max_length=45,null=True, blank=True, choices=[(None, 'Select'), ('12PT', '12pt'), ('14PT', '14pt'), ('16PT', '16pt'), ('18PT', '18pt'), ('20PT', '20pt'), ('22PT', '22pt'), ('CARD STOCK', 'card stock'), ('KRAFT STOCK', 'Kraft Stock'), ('CORRUGATED STOCK', 'Corrugated Stock'), ('RIGID STOCK', 'Rigid Stock'), ('OTHER', 'Other')])
    art_work=models.FileField(upload_to='art_work/', blank=True, null=True )
    full_name=models.CharField(max_length=45)
    email=models.EmailField()
    phone=models.IntegerField()
    notes=models.CharField(max_length=225)
    product = models.ForeignKey(Product, related_name="inquiries", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product