from django.urls import path
from . import views 

app_name = 'properties'

urlpatterns = [
    path('', views.property_list , name='property_list'),
    path('<slug:slug>', views.property_detail , name='property_detail'),
    path('category=<slug:category>', views.property_by_category , name = 'property_by_category'),
]
