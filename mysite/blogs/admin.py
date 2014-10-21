from django.contrib import admin
from blogs.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
  fields = ['tag', 'title', 'pub_date', 'context',]
admin.site.register(Blog, BlogAdmin)
