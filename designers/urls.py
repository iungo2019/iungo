from django.urls import path 
from .import views 

app_name = 'designers'

urlpatterns = [
	path('',views.designer_list , name = 'designer_list'), 
	path('<slug:slug>', views.designer_detail , name = 'designer_detail'),
	path('category=<slug:category>', views.designer_by_category , name = 'designer_by_category'),
]