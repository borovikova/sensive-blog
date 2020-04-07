from django.contrib import admin
from blog.models import Post, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "likes", )

class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "post",)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)