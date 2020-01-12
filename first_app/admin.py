from django.contrib import admin
from .models import Tag,Job

@admin.register(Job)
class PostAdmin(admin.ModelAdmin):
    pass
    # list_display = (['titel'])
    # list_filter = (['tags'])1

admin.site.register(Tag)
# admin.site.register(Job)
# admin.site.register(Cities)