from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from webapp.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager 

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	short_content = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	post_image = models.ImageField(upload_to='post/' ,null=True)
	profile_image = models.ImageField(upload_to='post_profile/' ,null=True)
	category = models.ForeignKey('Category' , null=True , on_delete=models.CASCADE)
	created = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(blank=True, null=True)
	tags = TaggableManager(blank=True)


	def save(self, *args, **kargs):
		if not self.slug and self.title :
			self.slug = slugify(self.title)
		super(Post , self).save(*args, **kargs)



	def __str__(self):
		return self.title


class Category(models.Model):
	category_name = models.CharField(max_length=50)



	def __str__(self):
		return self.category_name


	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


class Comment(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	post = models.ForeignKey(Post , on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.post.title
