from django.shortcuts import render , redirect
from .forms import ContactForm
# Create your views here.
from .models import ContactDetails
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse , HttpResponseRedirect
from blog.models import Post



def send_mail(request):
	contactdetails = ContactDetails.objects.last()
	post_list = Post.objects.all()
	template = 'contact/contact.html'


	if request.method == 'POST' :
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			subject = contact_form.cleaned_data['subject']
			your_email = contact_form.cleaned_data['your_email']
			message = contact_form.cleaned_data['message']

			try:
				sm(subject , your_email, message , ['hello@iungo.one'])


			except BadHeaderError:
				return HttpResponse ('invald error')

			return redirect('contact:sucess')



	else:
		contact_form = ContactForm()




	context = {
		'contactdetails' : contactdetails ,
		'contact_form' : contact_form ,
		'post_list' : post_list ,
	}

	return render(request, template , context)



def sucess(request):
	return HttpResponse ('mail sent sucessfully')
