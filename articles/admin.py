from django.contrib import admin
from .models import Article

# admin.site.register(Article)


# tuples and lists are both viable
# class ArticleAdmin(admin.ModelAdmin):
#     fields = ['title', 'author', 'created', 'edited']
#     readonly_fields = ('created', 'edited')
#     list_display = ['title', 'author', 'status']
#     list_filter = ('status',)
#     search_fields = ['title', 'author__username']
    
# admin.site.register(Article, ArticleAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "author", "slug")}),
        
        ("Important dates", {"fields": ("created", "edited")}),
        
        ("Content", {"fields": ("content", "image", "status")})
    )
    readonly_fields = ('created', 'edited', 'slug')
    list_display = ['title', 'author', 'status']
    list_filter = ('status',)
    search_fields = ['title', 'author__username']
    list_editable = ('status',)



