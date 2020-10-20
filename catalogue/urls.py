from . import views
from django.urls import path, include

urlpatterns = [
    path('<str:name>', views.catalogue_view, name="catalogue_by_name"),
    path('product/<int:id>', views.product_detail_view),

    #  product CRUD RESTRICTED ROUTES
]