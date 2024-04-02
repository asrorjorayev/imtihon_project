from django.contrib import admin
from .models import Tillar,Kitob,Comment

class KitobAdmin(admin.ModelAdmin):
    list_display=['id','name','kitob_beti','aftor','kitob_tili']
    list_display_links=['name','kitob_beti']
    search_fields=['aftor','kitob_tili']
admin.site.register(Kitob,KitobAdmin)

class TilAdmin(admin.ModelAdmin):
    list_display=['id','name']

admin.site.register(Tillar,TilAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id','user','kitob']
    list_display_links=['user','kitob']

admin.site.register(Comment,CommentAdmin)