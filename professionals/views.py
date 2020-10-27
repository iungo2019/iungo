from django.shortcuts import render
from .models import Professionals, Category, ProfessionalOffice, ProjectImages, Reserve
from .forms import ReserveForm
from django.core.paginator import Paginator
from django.db.models import Count
#from blog.models import Post

# Create your views here.




def professional_list(request):
	professional_list = Professionals.objects.all()
	category_list = Category.objects.annotate(total_professionals=Count('professionals'))
	#post_list = Post.objects.all()


	paginator = Paginator(professional_list , 6) # Show 25 contacts per page.
	page = request.GET.get('page')
	professional_list = paginator.get_page(page)


	context = {'professional_list' : professional_list , 'category_list' : category_list }


	return render (request, 'Professional/list.html', context)


def professional_detail(request, slug):
	professional_detail = Professionals.objects.get(slug=slug)
	professional_office_images = ProfessionalOffice.objects.filter(professional=professional_detail)
	project_images = ProjectImages.objects.filter(professional=professional_detail)

	if  request.method == 'POST':
		reserve_form = ReserveForm(request.POST)
		if reserve_form.is_valid():
			reserve_form.save()

	else:
		reserve_form = ReserveForm()


	context = {'professional_detail' : professional_detail , 'professional_office_images' : professional_office_images ,
	'project_images' : project_images , 'reserve_form' : reserve_form }


	return render (request, 'Professional/detail.html', context)


def professional_by_category(request , category):
	professional_by_category = Professionals.objects.filter(category__category_name=category)


	context = {'professional_list' : professional_by_category }


	return render (request, 'Professional/list.html', context)
