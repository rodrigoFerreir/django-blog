from django.contrib import admin

from .models import Post

# editando a class de Post no admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
