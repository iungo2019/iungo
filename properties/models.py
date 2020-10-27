from django.db import models
from django.utils.text import slugify


# Create your models here.


property_type = (
	('Sale' , "sale"),
	('Rent' , "rent"),
)


owner_type = (
	('Agent' , "agent"),
	('Owner' , "owner"),
)

swimming_pool = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)


gym = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)

fire_fighting_system  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)

club_house = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),

)

jogging_and_strolling = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)

reservred_parking  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)

power_backup  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)

bank_and_atm  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)


security  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)


earthquake_resistant  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)

intercom  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)


rainwater_harvesting  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)

lift  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)

visitor_parking  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
	('Not applicable', "Not applicable" ),
)

property_configrations = (
	('1 BHK' , '1 BHK'),
	('2 BHK' , '2 BHK'),
	('3 BHK' , '3 BHK'),
	('4 BHK' , '4 BHK'),
	('5 BHK' , '5 BHK'),
	('1,2 BHK' , '1,2 BHK'),
	('1,2,3 BHK' , '1,2,3 BHK'),
	('1,2,3,4 BHK' , '1,2,3,4 BHK'),
	('1,2,3,4,5 BHK' , '1,2,3,4,5 BHK'),

)


posession_status = (
	('January' , 'January'),
	('February' , 'February'),
	('March' , 'March'),
	('April' , 'April'),
	('May' , 'May'),
	('June' , 'June'),
	('July' , 'July'),
	('August' , 'August'),
	('Septmber' , 'Septmber'),
	('October' , 'October'),
	('November' , 'November'),
	('December' , 'December'),
	('Ready to move' , 'Ready to move'),
	('Not applicable', "Not applicable" ),

)

banks_approved = (
	('Axis Bank' , 'Axis Bank'),
	('Bandhan Bank' , 'Bandhan Bank'),
	('CSB Bank' , 'CSB Bank'),
	('City Union Bank' , 'City Union Bank'),
	('DCB Bank' , 'DCB Bank'),
	('Dhanlaxmi Bank' , 'Dhanlaxmi Bank'),
	('Federal Bank' , 'Federal Bank'),
	('HDFC Bank' , 'HDFC Bank'),
	('ICICI Bank' , 'ICICI Bank'),
	('IDBI Bank' , 'IDBI Bank'),
	('IDFC First Bank' , 'IDFC First Bank'),
	('IndusInd Bank' , 'IndusInd Bank'),
	('Karnataka Bank' , 'Ready to move'),
	('Karur Vysya Bank' , 'Karur Vysya Bank'),
	('Kotak Mahindra Bank' , 'Kotak Mahindra Bank'),
	('Lakshmi Vilas Bank' , 'Lakshmi Vilas Bank'),
	('Nainital Bank' , 'Nainital Bank'),
	('RBL Bank' , 'RBL Bank'),
	('South Indian Bank' , 'South Indian Bank'),
	('Tamilnad Mercantile Bank Limited' , 'Tamilnad Mercantile Bank Limited'),
	('Yes Bank' , 'Yes Bank'),


)




class Property(models.Model):
	name = models.CharField(max_length=50)
	builder_name = models.CharField(max_length=50 , null=True)
	owner_type = models.CharField(choices=owner_type ,max_length = 10 , null=True)
	property_type = models.CharField(choices=property_type ,max_length = 10)
	min_price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	max_price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	category = models.ForeignKey('Category', null=True ,on_delete=models.SET_NULL)
	average_price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	website = models.URLField(max_length=200, null=True)
	floor = models.PositiveIntegerField(null=True)
	profile_pic = models.ImageField(upload_to='propertyprofile_pic/' ,null=True)
	property_image= models.ImageField(upload_to='property_image/' ,null=True)
	experience = models.PositiveIntegerField(null=True)
	address = models.TextField()
	city = models.CharField(max_length=50, null=True)
	phone_number = models.CharField(max_length=15 ,null=True)
	phone_number_1 = models.CharField(max_length=15 ,null=True)
	email = models.EmailField(null=True)
	description = models.TextField(null=True)
	short_description = models.TextField(null=True)
	location = models.CharField(max_length=50, null=True)
	swimming_pool = models.CharField(choices=swimming_pool ,max_length = 20, null=True)
	gym = models.CharField(choices=gym ,max_length = 20, null=True)
	fire_fighting_system = models.CharField(choices=fire_fighting_system ,max_length = 20, null=True)
	club_house = models.CharField(choices=club_house ,max_length = 20, null=True)
	jogging_and_strolling = models.CharField(choices=jogging_and_strolling ,max_length = 20, null=True)
	reservred_parking = models.CharField(choices=reservred_parking ,max_length = 20, null=True)
	power_backup = models.CharField(choices=power_backup ,max_length = 20, null=True)
	bank_and_atm = models.CharField(choices=bank_and_atm ,max_length = 20, null=True)
	security = models.CharField(choices=security ,max_length = 20, null=True)
	earthquake_resistant = models.CharField(choices=earthquake_resistant ,max_length = 20, null=True)
	intercom = models.CharField(choices=intercom ,max_length = 20, null=True)
	rainwater_harvesting = models.CharField(choices=rainwater_harvesting ,max_length = 20, null=True)
	lift = models.CharField(choices=lift ,max_length = 20, null=True)
	visitor_parking = models.CharField(choices=visitor_parking ,max_length = 20, null=True)
	posession_status = models.CharField(choices=posession_status ,max_length = 20, null=True)
	posession_year = models.PositiveIntegerField(null=True)
	no_of_towers = models.PositiveIntegerField(null=True)
	no_of_units = models.PositiveIntegerField(null=True)
	project_area = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	rera_no = models.CharField(max_length=100, null=True)
	facebook_link = models.URLField(max_length=200, null=True)
	instagram_link = models.URLField(max_length=200, null=True)
	youtube_link = models.URLField(max_length=200, null=True)
	units_sold = models.PositiveIntegerField()
	units_available = models.PositiveIntegerField()
	total_units = models.PositiveIntegerField()
	slug = models.SlugField(blank=True, null=True)


	def save(self, *args, **kargs):
		if not self.slug and self.name :
			self.slug = slugify(self.name)
		super(Property , self).save(*args, **kargs)







	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Property'
		verbose_name_plural = 'Properties'




class Category(models.Model):
	category_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='category/' ,null=True)



	def __str__(self):
		return self.category_name


	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


class BuildersOffice(models.Model):
	property = models.ForeignKey(Property , on_delete=models.CASCADE)
	image = models.ImageField(upload_to='PropertyOffice/' , blank=True , null=True)


	def __str__(self):
		return self.property.builder_name



	class Meta:
		verbose_name = 'BuilderOffice'
		verbose_name_plural = 'BuildersOffice'


class Reserve(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone_number = models.CharField(max_length=15 ,null=True)

	def __str__(self):
		return self.name



class PropertyImages(models.Model):
	property = models.ForeignKey(Property , on_delete=models.CASCADE)
	image = models.ImageField(upload_to='projectproperty/' , blank=True , null=True)
	image_title = models.CharField(max_length=50, null=True)


	def __str__(self):
		return self.property.name

	class Meta:
		verbose_name = 'Property Image'
		verbose_name_plural = 'Property Images'



class Propertyarea(models.Model):
	property = models.ForeignKey(Property , on_delete=models.CASCADE)
	area = models.DecimalField(decimal_places=2 ,max_digits=10)
	area_configrations = models.CharField(choices=property_configrations ,max_length = 20, null=True)
	image = models.ImageField(upload_to='propertyfloor_plan/' , blank=True , null=True)
	floor_plan_title = models.CharField(max_length=50 , null=True)


	def __str__(self):
		return self.property.name



	class Meta:
		verbose_name = 'Property area'
		verbose_name_plural = 'Property areas'


class Banks_approved(models.Model):
	property = models.ForeignKey(Property, on_delete=models.CASCADE)
	banks_approved = models.CharField(choices=banks_approved ,max_length = 50, null=True)
	loan_details = models.TextField()


	def __str__(self):
		return self.property.name


	class Meta:
		verbose_name = 'Bank approved'
		verbose_name_plural = 'Banks approved'
