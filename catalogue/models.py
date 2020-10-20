from django.db import models

class Collection(models.Model):
    name=models.CharField(max_length=45)
    description=models.CharField(max_length=225)
    # featured = [list]
    # products = [list]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    display = models.ImageField(null=True, blank=True)
    featured_at=models.ForeignKey(Collection, related_name="featured", on_delete=models.CASCADE, null=True, blank=True)
    catalogue=models.ForeignKey(Collection, related_name="products", on_delete=models.CASCADE, null=True, blank=True)
    # inquiries = [list]
    # gallery = [list]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="gallery", default=None, on_delete=models.CASCADE)
    image =  models.ImageField(null=True, blank=True, upload_to='images')
    def __str__(self):
        return self.product.title    