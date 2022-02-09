from django.contrib import admin
from .models import Designer

# admin.site.register(Designer)


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    
    list_display = ('first_name', 'last_name', 'location')
    search_fields = ['first_name', 'last_name']

