from django.contrib import admin

# Register your models here.
from blog.models import *
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostFile)
admin.site.register(PostImage)