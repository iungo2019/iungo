from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Property , Category , PropertyImages , Propertyarea , Banks_approved , BuildersOffice
from django.db.models import Count
from .forms import ReserveForm
from blog.models import Post





def property_list(request):
	property_list = Property.objects.all()
	category_list = Category.objects.annotate(total_property=Count('property'))
	post_list = Post.objects.all()

	paginator = Paginator(property_list , 6) # Show 25 contacts per page.
	page = request.GET.get('page')
	property_list = paginator.get_page(page)


	context = {
		'property_list' : property_list , 'category_list' : category_list , 'post_list' : post_list
	}



	return render(request, 'Properties/list.html' , context)



def property_detail(request , slug):
	property_detail = Property.objects.get(slug=slug)
	property_images = PropertyImages.objects.filter(property=property_detail)
	builder_office_images = BuildersOffice.objects.filter(property=property_detail)
	property_area = Propertyarea.objects.filter(property=property_detail)
	banks_approved = Banks_approved.objects.filter(property=property_detail)
	post_list = Post.objects.all()
	template = 'property/detail.html'


	if  request.method == 'POST':
		reserve_form = ReserveForm(request.POST)
		if reserve_form.is_valid():
			reserve_form.save()

	else:
		reserve_form = ReserveForm()




	context = {
		'property_detail' : property_detail , 'property_images' : property_images ,
		'reserve_form' : reserve_form , 'property_area' : property_area , 'banks_approved' : banks_approved ,
		'builder_office_images' : builder_office_images , 'post_list' : post_list
	}

	return render(request, 'Properties/detail.html' , context)



def property_by_category(request , category):
	property_by_category = Property.objects.filter(category__category_name=category)


	context = {'property_list' : property_by_category }


	return render (request, 'Properties/list.html', context)
