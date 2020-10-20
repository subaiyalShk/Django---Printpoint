from django.urls import path, include
from admindash import views

urlpatterns = [
    path('', views.dashboard, name='office'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('inquire/<int:id>', views.createInquiry, name='inquire'),
    path('inquiries/', views.inquiries_view, name='inquiries'),
    
    path('product/new/catalogue/<str:name>', views.productCreate, name='create_product'),
    path('product/<int:id>/edit/<str:name>', views.productUpdate),
    path('product/<int:id>/delete/<str:name>', views.productDelete, name='delete_product'),

    path('user_logout', views.user_logout, name='user_logout'),
    path('admin_catalogue/<str:name>', views.catalogue_view, name='admin_catalogue'),
    
]