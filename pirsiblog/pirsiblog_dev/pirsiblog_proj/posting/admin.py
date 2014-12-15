from django.contrib import admin
from posting.models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def delete_post():
        pass
    

admin.site.register(Post, PostAdmin)
