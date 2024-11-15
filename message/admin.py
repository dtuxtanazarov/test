from django.contrib import admin


from .models import Post, Category, Region


# Register your models here.
# class Category_admin(admin.ModelAdmin):
#     list_display = ['id','name']
# class Region_admin(admin.ModelAdmin):
#     list_display = ['id','name']
# class Post_admin(admin.ModelAdmin):
#     list_display = ('category','region','id','title','body','author','date')
admin.site.register(Post )
admin.site.register(Category)
admin.site.register(Region)