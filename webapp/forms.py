from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Customer, Designer, Architect, Builder, Agent, Support_staff, Category, Cloud , AgentProperty, AddProperty


#----------------------------   Customer Side -----------------------------------------#

class CustomerRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self, commit=True):
			user = super().save(commit=False)
			user.is_customer=True
			if commit:
				user.save()
			return user


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['first_name','last_name','city','phone','address', 'profile_pic']



class CustomerCloudForm(forms.ModelForm):
	class Meta:
		model = Cloud
		fields = ['project_name','professional_name','file_type','upload_file','Notes']



#----------------------------   Designer Side -----------------------------------------#



class DesignerRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self,commit=True):
			user=super().save(commit=False)
			user.is_designer=True
			if commit:
				user.save()
			return user

class DesignerForm(forms.ModelForm):
	class Meta:
		model = Designer
		fields = ['full_name','email','phone_number','company_name','pincode', 'website', 'company_address', 'company_logo']


#----------------------------   Architect Side -----------------------------------------#

class ArchitectRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self,commit=True):
			user=super().save(commit=False)
			user.is_architect=True
			if commit:
				user.save()
			return user

class ArchitectForm(forms.ModelForm):
	class Meta:
		model = Architect
		fields = ['full_name','email','phone_number','company_name','pincode', 'website', 'company_address', 'company_logo']

#----------------------------   Builder Side -----------------------------------------#

class BuilderRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self,commit=True):
			user=super().save(commit=False)
			user.is_builder=True
			if commit:
				user.save()
			return user


class BuilderForm(forms.ModelForm):
	class Meta:
		model = Builder
		fields = ['full_name','email','phone_number','company_name','pincode', 'website', 'company_address', 'company_logo']

class BuilderPropertyForm(forms.ModelForm):
	class Meta:
		model = AddProperty
		fields = ['property_name','property_category','property_location','upload_property_image', 'Description']


#----------------------------   Agent Side -----------------------------------------#

class AgentRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self,commit=True):
			user=super().save(commit=False)
			user.is_agent=True
			if commit:
				user.save()
			return user

class AgentForm(forms.ModelForm):
	class Meta:
		model = Agent
		fields = ['full_name','email','phone_number','company_name','pincode', 'website', 'company_address', 'company_logo']


class AgentPropertyForm(forms.ModelForm):
	class Meta:
		model = AgentProperty
		fields = ['property_name','property_category','property_type','property_location','upload_property_image', 'Description']


#----------------------------   Support_staff Side -----------------------------------------#

class Support_staffRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self,commit=True):
			user=super().save(commit=False)
			user.is_support_staff=True
			if commit:
				user.save()
			return user


class Support_staffForm(forms.ModelForm):
	class Meta:
		model = Support_staff
		fields = ['full_name','category','email','phone_number','company_name','pincode', 'website', 'company_address', 'company_logo']
