from django.contrib import admin
from .models import Book, PublicBook
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(PublicBook)
class PublicBookAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Use the correct database
        return super().get_queryset(request).using('public_library')

    def save_model(self, request, obj, form, change):
        # Save to the correct database
        obj.save(using='public_library')

    def delete_model(self, request, obj):
        # Delete from the correct database
        obj.delete(using='public_library')