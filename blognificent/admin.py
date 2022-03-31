from django.contrib import admin

# Register your models here.
from blognificent.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['text']}),
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
