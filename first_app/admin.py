from django.contrib import admin
from .models import Tag,Job
#
# @admin.register(Job)
# class PostAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Tag)
admin.site.register(Job)