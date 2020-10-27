from django.contrib import admin

# Register your models here.
from .models import ( User, Customer, Designer, Architect, Builder, Agent, Support_staff, Category ,
                    Cloud , DesignerEnquries, ArchitectEnquries, BuilderEnquries, AgentEnquries, SupportEnquries ,
                    AgentProperty, AddProperty )


admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Designer)
admin.site.register(Architect)
admin.site.register(Builder)
admin.site.register(Agent)
admin.site.register(Support_staff)
admin.site.register(Category)
admin.site.register(Cloud)
admin.site.register(DesignerEnquries)
admin.site.register(ArchitectEnquries)
admin.site.register(BuilderEnquries)
admin.site.register(AgentEnquries)
admin.site.register(SupportEnquries)
admin.site.register(AgentProperty)
admin.site.register(AddProperty)
