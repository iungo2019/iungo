from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils import timezone


class User(AbstractUser):
    is_customer           = models.BooleanField(default=False)
    is_designer           = models.BooleanField(default=False)
    is_architect          = models.BooleanField(default=False)
    is_builder            = models.BooleanField(default=False)
    is_agent              = models.BooleanField(default=False)
    is_support_staff      = models.BooleanField(default=False)


File_Type  = (
	('Design' , "Design"),
	('Estimation' , "Estimation"),
    ('Quotation',"Quotation"),
    ('Invoice', "Invoice"),
    ('Bills', "Bills"),
)

Property_Type  = (
	('For Rent' , "For Rent"),
	('For Sale' , "For Sale"),
)

Property_Category = (
    ('Villa' , "Villa"),
	('Flat' , "Flat"),
    ('Independent_house' , "Independent_house"),
    ('Cosharing' , "Cosharing"),
)
#----------------------------   Customer Side -----------------------------------------#


class Customer(models.Model):
    user 		= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=20,blank=False)
    last_name	= models.CharField(max_length=20,blank=False)
    city  		= models.CharField(max_length=40,blank=False)
    phone 		= models.CharField(max_length=10,blank=False)
    address		= models.TextField()
    profile_pic = models.ImageField(null=True, blank=True)


    def __str__(self):
    	return self.user.username


class Cloud(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=20, blank=False)
    professional_name = models.CharField(max_length=20, blank=False)
    file_type = models.CharField(choices=File_Type , max_length = 50, null=True)
    upload_file = models.FileField(null=True, blank=True)
    Notes = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.professional_name

    class Meta:
    	verbose_name = 'CustomerCloud'
    	verbose_name_plural = 'CustomersCloud'


#----------------------------   Designer Side -----------------------------------------#

profile_status = (
    ('Verifing' , "Verifing"),
    ('Details_required' , "Details_required"),
    ('Profile_created',"Profile_created"),
    ('Awaiting_confiramtion', "Awaiting_confiramtion"),
    ('Profile_live', "Profile_live"),
)

class Designer(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    full_name               = models.CharField(max_length=50)
    email                   = models.EmailField(null=True)
    phone_number            = models.CharField(max_length=15 ,null=True)
    company_name            = models.CharField(max_length=50 ,null=True)
    pincode                 = models.PositiveIntegerField(null=True)
    website                 = models.URLField(max_length=200, null=True)
    company_address         = models.TextField(null=True)
    company_logo            = models.ImageField(null=True, blank=True)
    profile_status          = models.CharField(choices=profile_status , max_length = 50, null=True)


    def __str__(self):
    	return self.full_name


    class Meta:
    	verbose_name = 'Designer'
    	verbose_name_plural = 'Designers'


class DesignerEnquries(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=20, blank=False)
    project_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15 ,null=True)
    Requirements = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.customer_name

    class Meta:
    	verbose_name = 'DesignerEnquiry'
    	verbose_name_plural = 'DesignerEnquries'


#----------------------------   Architect Side -----------------------------------------#

class Architect(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    full_name               = models.CharField(max_length=50)
    email                   = models.EmailField(null=True)
    phone_number            = models.CharField(max_length=15 ,null=True)
    company_name            = models.CharField(max_length=50 ,null=True)
    pincode                 = models.PositiveIntegerField(null=True)
    website                 = models.URLField(max_length=200, null=True)
    company_address         = models.TextField(null=True)
    company_logo            = models.ImageField(null=True, blank=True)
    profile_status          = models.CharField(choices=profile_status , max_length = 50, null=True)


    def __str__(self):
    	return self.full_name


    class Meta:
    	verbose_name = 'Architect'
    	verbose_name_plural = 'Architects'

class ArchitectEnquries(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=20, blank=False)
    project_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15 ,null=True)
    Requirements = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.customer_name

    class Meta:
    	verbose_name = 'ArchitectEnquiry'
    	verbose_name_plural = 'ArchitectEnquries'

#----------------------------   Builder Side -----------------------------------------#

class Builder(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    full_name               = models.CharField(max_length=50)
    email                   = models.EmailField(null=True)
    phone_number            = models.CharField(max_length=15 ,null=True)
    company_name            = models.CharField(max_length=50 ,null=True)
    pincode                 = models.PositiveIntegerField(null=True)
    website                 = models.URLField(max_length=200, null=True)
    company_address         = models.TextField(null=True)
    company_logo            = models.ImageField(null=True, blank=True)
    profile_status          = models.CharField(choices=profile_status , max_length = 50, null=True)


    def __str__(self):
    	return self.full_name


    class Meta:
    	verbose_name = 'Builder'
    	verbose_name_plural = 'Builders'


class BuilderEnquries(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=20, blank=False)
    project_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15 ,null=True)
    Requirements = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.customer_name

    class Meta:
    	verbose_name = 'BuilderEnquiry'
    	verbose_name_plural = 'BuilderEnquries'


class AddProperty(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    property_name = models.CharField(max_length=20, blank=False)
    property_category = models.CharField(choices=Property_Category , max_length = 50, null=True)
    property_location = models.CharField(max_length = 50, null=True)
    upload_property_image = models.FileField(null=True, blank=True)
    Description = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.property_name

    class Meta:
    	verbose_name = 'AddProperty'
    	verbose_name_plural = 'AddProperties'


#----------------------------   Agent Side -----------------------------------------#

class Agent(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    full_name               = models.CharField(max_length=50)
    email                   = models.EmailField(null=True)
    phone_number            = models.CharField(max_length=15 ,null=True)
    company_name            = models.CharField(max_length=50 ,null=True)
    pincode                 = models.PositiveIntegerField(null=True)
    website                 = models.URLField(max_length=200, null=True)
    company_address         = models.TextField(null=True)
    company_logo            = models.ImageField(null=True, blank=True)
    profile_status          = models.CharField(choices=profile_status , max_length = 50, null=True)


    def __str__(self):
    	return self.full_name


    class Meta:
    	verbose_name = 'Agent'
    	verbose_name_plural = 'Agents'

class AgentEnquries(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=20, blank=False)
    project_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15 ,null=True)
    Requirements = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.customer_name

    class Meta:
    	verbose_name = 'AgentEnquiry'
    	verbose_name_plural = 'AgentEnquries'

class AgentProperty(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    property_name = models.CharField(max_length=20, blank=False)
    property_category = models.CharField(choices=Property_Category , max_length = 50, null=True)
    property_type = models.CharField(choices=Property_Type , max_length = 50, null=True)
    property_location = models.CharField(max_length = 50, null=True)
    upload_property_image = models.FileField(null=True, blank=True)
    Description = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.property_name

    class Meta:
    	verbose_name = 'AgentProperty'
    	verbose_name_plural = 'AgentProperties'

#----------------------------   Support_staff Side -----------------------------------------#

class Support_staff(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    full_name               = models.CharField(max_length=50)
    email                   = models.EmailField(null=True)
    phone_number            = models.CharField(max_length=15 ,null=True)
    company_name            = models.CharField(max_length=50 ,null=True)
    category                = models.ForeignKey('Category', null=True ,on_delete=models.SET_NULL)
    pincode                 = models.PositiveIntegerField(null=True)
    website                 = models.URLField(max_length=200, null=True)
    company_address         = models.TextField(null=True)
    company_logo            = models.ImageField(null=True, blank=True)
    profile_status          = models.CharField(choices=profile_status , max_length = 50, null=True)

    def __str__(self):
    	return self.full_name


    class Meta:
    	verbose_name = 'Support_staff'
    	verbose_name_plural = 'Support_staffs'


class Category(models.Model):
    category_name = models.CharField(max_length=50)


    def __str__(self):
    	return self.category_name



    class Meta:
    	verbose_name = 'Category'
    	verbose_name_plural = 'Categories'


class SupportEnquries(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=20, blank=False)
    project_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15 ,null=True)
    Requirements = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.customer_name

    class Meta:
    	verbose_name = 'SupportEnquiry'
    	verbose_name_plural = 'SupportEnquries'
