from django.urls import path
from .import views

app_name = 'professionals'

urlpatterns = [
	path('',views.professional_list , name = 'professional_list'),
	path('<slug:slug>', views.professional_detail , name = 'professional_detail'),
	path('category=<slug:category>', views.professional_by_category , name = 'professional_by_category'),
]
