from django.contrib import admin
from .models import BlogPost, BlogComment, BlogCategory

admin.site.register(BlogCategory)
admin.site.register(BlogComment)


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    model = BlogPost

    list_display = (
        "id",
        "title",
        "slug",
        "date_created",
    )
    list_filter = (
        "date_created",
        "date_updated",
    )
    list_editable = (
        "title",
        "slug",
    )
    search_fields = (
        "title",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
        )
    }
    date_hierarchy = "date_created"
    save_on_top = True
