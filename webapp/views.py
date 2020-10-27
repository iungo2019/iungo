from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from .forms import (CustomerRegisterForm, DesignerRegisterForm, ArchitectRegisterForm,
 					BuilderRegisterForm,AgentRegisterForm, Support_staffRegisterForm,
					CustomerForm, DesignerForm, ArchitectForm, BuilderForm, AgentForm,
					Support_staffForm, CustomerCloudForm, AgentPropertyForm, BuilderPropertyForm)
from django.contrib.auth.decorators import login_required
from collections import Counter
from django.urls import reverse
from django.db.models import Q
from .models import ( User, Customer, Designer, Architect, Builder, Agent, Support_staff, Category ,
                    Cloud , DesignerEnquries,ArchitectEnquries, BuilderEnquries, AgentEnquries, SupportEnquries,
                    AddProperty, AgentProperty)
from django.core.paginator import Paginator



#----------------------------   Customer Side -----------------------------------------#

def customerRegister(request):
	form =CustomerRegisterForm(request.POST or None)
	if form.is_valid():
		user      = form.save(commit=False)
		username  =	form.cleaned_data['username']
		password  = form.cleaned_data['password']
		user.is_customer=True
		user.set_password(password)
		user.save()
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/user/create/")

	context ={
		'form':form
	}
	return render(request,'webapp/signup.html',context)


def customerLogin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user     = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/profile/user/")
			else:
				return render(request,'webapp/login.html',{'error_message':'Your account disable'})
		else:
			return render(request,'webapp/login.html',{'error_message': 'Invalid Login'})
	return render(request,'webapp/login.html')


def customerProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user

	return render(request,'webapp/profile.html', {'user': user})

def createCustomer(request):
	form = CustomerForm(request.POST , request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("/profile/user/")
	context={
	'form':form,
	'title':"Complete Your profile"
	}
	return render(request,'webapp/profile_form.html',context)


def updateCustomer(request,id):
	form  	 = CustomerForm(request.POST or None,request.FILES or None,instance=request.user.customer)
	if form.is_valid():
		form.save()
		return redirect("/profile/user/")
	context={
	'form':form,
	'title':"Update Your profile"
	}
	return render(request,'webapp/profile_form.html',context)


def CustomerCloud(request):
	form = CustomerCloudForm(request.POST , request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect ("/profile/user")
	context={
	'form':form,
	}
	return render(request,'webapp/cloudupload.html',context)


def record_list(request):
	record_list = Cloud.objects.filter(user=request.user)

	paginator = Paginator(record_list , 4) # Show 25 contacts per page.
	page = request.GET.get('page')
	record_list = paginator.get_page(page)





	context = { 'record_list' : record_list}

	return render(request,'webapp/records.html',context)








#----------------------------   Designer Side -----------------------------------------#




def designerRegister(request):
	form =DesignerRegisterForm(request.POST or None)
	if form.is_valid():
		user      = form.save(commit=False)
		username  =	form.cleaned_data['username']
		password  = form.cleaned_data['password']
		user.is_designer=True
		user.set_password(password)
		user.save()
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/designer/create/")
	context ={
		'form':form
	}
	return render(request,'webapp/designersignup.html',context)



def designerLogin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user     = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/profile/designer/")
			else:
				return render(request,'webapp/designerlogin.html',{'error_message':'Your account disable'})
		else:
			return render(request,'webapp/designerlogin.html',{'error_message': 'Invalid Login'})
	return render(request,'webapp/designerlogin.html')





def designerProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user



	return render(request,'webapp/designer_profile.html', {'user': user})



@login_required(login_url='/login/designer/')
def createDesigner(request):
	form=DesignerForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("/profile/designer/")
	context={
	'form':form,
	'title':"Complete Your profile"
	}
	return render(request,'webapp/designer_profile_form.html',context)

#Update restaurant detail
@login_required(login_url='/login/designer/')
def updateDesigner(request,id):
	form  	 = DesignerForm(request.POST or None,request.FILES or None,instance=request.user.designer)
	if form.is_valid():
		form.save()
		return redirect('/profile/designer/')
	context={
	'form':form,
	'title':"Update Your profile"
	}
	return render(request,'webapp/designer_profile_form.html',context)



@login_required(login_url='/login/designer/')
def EnquiryDesigner(request):
	enquiry_list = DesignerEnquries.objects.filter(user=request.user)

	paginator = Paginator(enquiry_list , 4) # Show 25 contacts per page.
	page = request.GET.get('page')
	record_list = paginator.get_page(page)





	context = { 'enquiry_list' : enquiry_list}

	return render(request,'webapp/designerenquiry.html',context)


#----------------------------   Architect Side -----------------------------------------#

def architectRegister(request):
	form = ArchitectRegisterForm(request.POST or None)
	if form.is_valid():
		user      = form.save(commit=False)
		username  =	form.cleaned_data['username']
		password  = form.cleaned_data['password']
		user.is_architect=True
		user.set_password(password)
		user.save()
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/architect/create/")
	context ={
		'form':form
	}
	return render(request,'webapp/architectsignup.html',context)



def architectLogin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user     = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/profile/architect/")
			else:
				return render(request,'webapp/architectlogin.html',{'error_message':'Your account disable'})
		else:
			return render(request,'webapp/architectlogin.html',{'error_message': 'Invalid Login'})
	return render(request,'webapp/architectlogin.html')





def architectProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user



	return render(request,'webapp/architect_profile.html', {'user': user})



@login_required(login_url='/login/architect/')
def createArchitect(request):
	form=ArchitectForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("/profile/architect/")
	context={
	'form':form,
	'title':"Complete Your profile"
	}
	return render(request,'webapp/architect_profile_form.html',context)

#Update restaurant detail
@login_required(login_url='/login/architect/')
def updateArchitect(request,id):
	form  	 = ArchitectForm(request.POST or None,request.FILES or None,instance=request.user.architect)
	if form.is_valid():
		form.save()
		return redirect('/profile/architect/')
	context={
	'form':form,
	'title':"Update Your profile"
	}
	return render(request,'webapp/architect_profile_form.html',context)



@login_required(login_url='/login/architect/')
def EnquiryArchitect(request):
	aenquiry_list = ArchitectEnquries.objects.filter(user=request.user)

	paginator = Paginator(aenquiry_list , 4) # Show 25 contacts per page.
	page = request.GET.get('page')
	aenquiry_list= paginator.get_page(page)





	context = { 'aenquiry_list' : aenquiry_list}

	return render(request,'webapp/architectenquiry.html',context)




#----------------------------   Builder Side -----------------------------------------#



def builderRegister(request):
	form = BuilderRegisterForm(request.POST or None)
	if form.is_valid():
		user      = form.save(commit=False)
		username  =	form.cleaned_data['username']
		password  = form.cleaned_data['password']
		user.is_builder = True
		user.set_password(password)
		user.save()
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/builder/create/")
	context ={
		'form':form
	}
	return render(request,'webapp/buildersignup.html',context)



def builderLogin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user     = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/profile/builder/")
			else:
				return render(request,'webapp/builderlogin.html',{'error_message':'Your account disable'})
		else:
			return render(request,'webapp/builderlogin.html',{'error_message': 'Invalid Login'})
	return render(request,'webapp/builderlogin.html')





def builderProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user



	return render(request,'webapp/builder_profile.html', {'user': user})



@login_required(login_url='/login/builder/')
def createBuilder(request):
	form=BuilderForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("/profile/builder/")
	context={
	'form':form,
	'title':"Complete Your profile"
	}
	return render(request,'webapp/builder_profile_form.html',context)

#Update restaurant detail
@login_required(login_url='/login/builder/')
def updateBuilder(request,id):
	form  	 = BuilderForm(request.POST or None,request.FILES or None,instance=request.user.builder)
	if form.is_valid():
		form.save()
		return redirect('/profile/builder/')
	context={
	'form':form,
	'title':"Update Your profile"
	}
	return render(request,'webapp/builder_profile_form.html',context)



@login_required(login_url='/login/builder/')
def EnquiryBuilder(request):
	benquiry_list = BuilderEnquries.objects.filter(user=request.user)

	paginator = Paginator(benquiry_list , 4) # Show 25 contacts per page.
	page = request.GET.get('page')
	benquiry_list= paginator.get_page(page)





	context = { 'benquiry_list' : benquiry_list}

	return render(request,'webapp/builderenquiry.html',context)

@login_required(login_url='/login/builder/')
def AddBuilderProperties(request):
	form = BuilderPropertyForm(request.POST , request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect ("/profile/builder")
	context={
	'form':form,
	}
	return render(request,'webapp/builderproperty.html',context)


@login_required(login_url='/login/builder/')
def BuilderProperty(request):
	bproperty_list = AddProperty.objects.filter(user=request.user)

	paginator = Paginator(bproperty_list , 4) # Show 25 contacts per page.
	page = request.GET.get('page')
	bproperty_list= paginator.get_page(page)


	context = { 'bproperty_list' : bproperty_list}

	return render(request,'webapp/builderproperties.html',context)


#----------------------------   Agent Side -----------------------------------------#


def agentRegister(request):
	form = AgentRegisterForm(request.POST or None)
	if form.is_valid():
		user      = form.save(commit=False)
		username  =	form.cleaned_data['username']
		password  = form.cleaned_data['password']
		user.is_agent = True
		user.set_password(password)
		user.save()
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/agent/create/")
	context ={
		'form':form
	}
	return render(request,'webapp/agentsignup.html',context)



def agentLogin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user     = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/profile/agent/")
			else:
				return render(request,'webapp/agentlogin.html',{'error_message':'Your account disable'})
		else:
			return render(request,'webapp/agentlogin.html',{'error_message': 'Invalid Login'})
	return render(request,'webapp/agentlogin.html')





def agentProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user



	return render(request,'webapp/agent_profile.html', {'user': user})



@login_required(login_url='/login/agent/')
def createAgent(request):
	form=AgentForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("/profile/agent/")
	context={
	'form':form,
	'title':"Complete Your profile"
	}
	return render(request,'webapp/agent_profile_form.html',context)

#Update restaurant detail
@login_required(login_url='/login/agent/')
def updateAgent(request,id):
	form  	 = AgentForm(request.POST or None,request.FILES or None,instance=request.user.agent)
	if form.is_valid():
		form.save()
		return redirect('/profile/agent/')
	context={
	'form':form,
	'title':"Update Your profile"
	}
	return render(request,'webapp/agent_profile_form.html',context)



@login_required(login_url='/login/agent/')
def EnquiryAgent(request):
	agenquiry_list = AgentEnquries.objects.filter(user=request.user)

	paginator = Paginator(agenquiry_list , 4) # Show 25 contacts per page.
	page = request.GET.get('page')
	agenquiry_list= paginator.get_page(page)


	context = { 'agenquiry_list' : agenquiry_list}

	return render(request,'webapp/agentenquiry.html',context)


@login_required(login_url='/login/agent/')
def AddAgentProperties(request):
	form = AgentPropertyForm(request.POST , request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect ("/profile/agent")
	context={
	'form':form,
	}
	return render(request,'webapp/agentproperty.html',context)


@login_required(login_url='/login/agent/')
def AgentProperties(request):
	agproperty_list = AgentProperty.objects.filter(user=request.user)

	paginator = Paginator(agproperty_list , 4) # Show 25 contacts per page.
	page = request.GET.get('page')
	agproperty_list= paginator.get_page(page)


	context = { 'agproperty_list' : agproperty_list}

	return render(request,'webapp/agentproperties.html',context)


#----------------------------   Support_staff Side -----------------------------------------#



def supportRegister(request):
	form = Support_staffRegisterForm(request.POST or None)
	if form.is_valid():
		user      = form.save(commit=False)
		username  =	form.cleaned_data['username']
		password  = form.cleaned_data['password']
		user.is_support_staff = True
		user.set_password(password)
		user.save()
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/support/create/")
	context ={
		'form':form
	}
	return render(request,'webapp/supportsignup.html',context)



def supportLogin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user     = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/profile/support/")
			else:
				return render(request,'webapp/supportlogin.html',{'error_message':'Your account disable'})
		else:
			return render(request,'webapp/supportlogin.html',{'error_message': 'Invalid Login'})
	return render(request,'webapp/supportlogin.html')





def supportProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user



	return render(request,'webapp/support_profile.html', {'user': user})



@login_required(login_url='/login/agent/')
def createSupport(request):
	form=Support_staffForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("/profile/support/")
	context={
	'form':form,
	'title':"Complete Your profile"
	}
	return render(request,'webapp/support_profile_form.html',context)

#Update restaurant detail
@login_required(login_url='/login/agent/')
def updateSupport(request,id):
	form  	 = Support_staffForm(request.POST or None,request.FILES or None,instance=request.user.support_staff)
	if form.is_valid():
		form.save()
		return redirect('/profile/support/')
	context={
	'form':form,
	'title':"Update Your profile"
	}
	return render(request,'webapp/support_profile_form.html',context)



@login_required(login_url='/login/support/')
def EnquirySupport(request):
	senquiry_list = SupportEnquries.objects.filter(user=request.user)

	paginator = Paginator(senquiry_list , 4) # Show 25 contacts per page.
	page = request.GET.get('page')
	senquiry_list= paginator.get_page(page)





	context = { 'senquiry_list' : senquiry_list}

	return render(request,'webapp/supportenquiry.html',context)



#---------------------------- Logout View -----------------------------------------#



def Logout(request):
    if request.user.is_designer:
        logout(request)
        return redirect("/login/designer/")

    elif request.user.is_architect:
        logout(request)
        return redirect("/login/architect/")

    elif request.user.is_builder:
        logout(request)
        return redirect("/login/builder/")

    elif request.user.is_agent:
        logout(request)
        return redirect("/login/agent/")

    elif request.user.is_support_staff:
        logout(request)
        return redirect("/login/support/")


    else:
        logout(request)
        return redirect("/login/user/")
