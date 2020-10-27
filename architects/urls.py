from django.urls import path
from .import views

app_name = 'architects'

urlpatterns = [
	path('',views.architect_list , name = 'architect_list'),
	path('<slug:slug>', views.architect_detail , name = 'architect_detail'),
	path('category=<slug:category>', views.architect_by_category , name = 'architect_by_category'),
]
