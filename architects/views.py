from django.shortcuts import render
from .models import Architects , Category , ArchitectOffice , Banks_approved , ProjectImages , Reserve , Style
from .forms import ReserveForm
from django.db.models import Count
from django.core.paginator import Paginator
from blog.models import Post


def architect_list(request):
	architect_list = Architects.objects.all()
	category_list = Category.objects.annotate(total_architects=Count('architects'))
	style_list = Style.objects.annotate(total_architects=Count('architects'))
	post_list = Post.objects.all()

	paginator = Paginator(architect_list , 6) # Show 25 contacts per page.
	page = request.GET.get('page')
	architect_list = paginator.get_page(page)


	context = {'architect_list' : architect_list , 'category_list' : category_list , 'post_list' : post_list ,
	'style_list' : style_list }


	return render (request, 'Architect/list.html', context)


def architect_detail(request, slug):
	architect_detail = Architects.objects.get(slug=slug)
	architect_office_images = ArchitectOffice.objects.filter(architect=architect_detail)
	banks_approved = Banks_approved.objects.filter(architect=architect_detail)
	project_images = ProjectImages.objects.filter(architect=architect_detail)
	post_list = Post.objects.all()

	if  request.method == 'POST':
		reserve_form = ReserveForm(request.POST)
		if reserve_form.is_valid():
			reserve_form.save()

	else:
		reserve_form = ReserveForm()


	context = {'architect_detail' : architect_detail , 'architect_office_images' : architect_office_images , 'banks_approved' : banks_approved ,
	'project_images' : project_images , 'reserve_form' : reserve_form }


	return render (request, 'Architect/detail.html', context)


def architect_by_category(request , category):
	architect_by_category = Architects.objects.filter(category__category_name=category)


	context = {'architect_list' : architect_by_category , 'post_list' : post_list }


	return render (request, 'Architect/list.html', context)
