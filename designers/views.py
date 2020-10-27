from django.shortcuts import render
from .models import Designers , DesignerOffice , Banks_approved , ProjectImages , Reserve , Category , Style
from .forms import ReserveForm
from django.core.paginator import Paginator
from django.db.models import Count
from blog.models import Post

# Create your views here.




def designer_list(request):
	designer_list = Designers.objects.all()
	category_list = Category.objects.annotate(total_designers=Count('designers'))
	style_list = Style.objects.annotate(total_designers=Count('designers'))

	post_list = Post.objects.all()


	paginator = Paginator(designer_list , 6) # Show 25 contacts per page.
	page = request.GET.get('page')
	designer_list = paginator.get_page(page)


	context = {'designer_list' : designer_list , 'category_list' : category_list , 'style_list' : style_list , 'post_list' : post_list}


	return render (request, 'Designer/list.html', context)


def designer_detail(request, slug):
	designer_detail = Designers.objects.get(slug=slug)
	designer_office_images = DesignerOffice.objects.filter(designer=designer_detail)
	banks_approved = Banks_approved.objects.filter(designer=designer_detail)
	project_images = ProjectImages.objects.filter(designer=designer_detail)
	post_list = Post.objects.all()

	if  request.method == 'POST':
		reserve_form = ReserveForm(request.POST)
		if reserve_form.is_valid():
			reserve_form.save()

	else:
		reserve_form = ReserveForm()


	context = {'designer_detail' : designer_detail , 'designer_office_images' : designer_office_images , 'banks_approved' : banks_approved ,
	'project_images' : project_images , 'reserve_form' : reserve_form , 'post_list' : post_list }


	return render (request, 'Designer/detail.html', context)


def designer_by_category(request , category):
	designer_by_category = Designers.objects.filter(category__category_name=category)


	context = {'designer_list' : designer_by_category }


	return render (request, 'Designer/list.html', context)
