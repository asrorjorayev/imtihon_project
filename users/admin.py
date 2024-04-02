from django.contrib import admin
from .models import User

class AdminUser(admin.ModelAdmin):
    list_display=['id','username','first_name','phone_number']
    list_display_links=['id','username']
    search_fields=['username','phone_number']
admin.site.register(User,AdminUser)