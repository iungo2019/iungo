from django.contrib import admin

# Register your models here.
from .models import Designers , Category , DesignerOffice , Banks_approved , ProjectImages , Reserve , Style

admin.site.register(Designers)
admin.site.register(Category)
admin.site.register(DesignerOffice)
admin.site.register(Banks_approved)
admin.site.register(ProjectImages)
admin.site.register(Reserve)
admin.site.register(Style)