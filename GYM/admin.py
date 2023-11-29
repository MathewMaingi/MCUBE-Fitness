from django.contrib import admin
from GYM.models import Member, Contact, Trainer, RecentPost, Blog, ImageModel, Subscription, ClassModel

# Register your models here.

admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(Trainer)
admin.site.register(Blog)
admin.site.register(ImageModel)
admin.site.register(ClassModel)
admin.site.register(Subscription)
admin.site.register(RecentPost)