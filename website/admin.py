from django.contrib import admin
from .models import Contact, Newsletter

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'created_date']
    list_filter = ['email']
    


admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)