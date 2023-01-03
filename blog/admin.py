from django.contrib import admin
from .models import Post,Contact_Us,Like
# Register your models here.

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['title','description','published_at','author']


@admin.register(Contact_Us)
class Contact_us_ModellAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile','message']

@admin.register(Like)
class Like_ModelAdmin(admin.ModelAdmin):
    list_display=['created_at','user','like']