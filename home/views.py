from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.db.models import Count

# Create your views here.
from designers.models import Designers
from .models import Home , Testinomials
from properties.models import Property
from architects.models import Architects
from blog.models import Post




def home(request):
	home = Home.objects.last()
	testinomial_list = Testinomials.objects.all()
	designer_list = Designers.objects.all()
	property_list = Property.objects.all()
	architect_list = Architects.objects.all()
	post_list = Post.objects.all()




	context = {
		'designer_list_home' : designer_list ,
		'property_list_home' : property_list ,
		'home' : home ,
		'architect_list_home' : architect_list ,
		'post_list' : post_list ,
		'testinomial_list' : testinomial_list ,
    }

	return render (request , 'Home/home1.html' , context)
