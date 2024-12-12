from django.contrib import admin

# Register your models here.

from django.contrib import admin
from trash_classify.models import HisData

admin.site.register(HisData)

# Custom admin class to control the admin form behavior
# class HisDataAdmin(admin.ModelAdmin):
#     readonly_fields = ('add_date',)  # Make 'add_date' read-only

#     # Optional: Control the order of the fields in the form
#     fields = ('image', 'label', 'label_name', 'add_date')  # Order of fields

#     # Optional: Show these fields in the list view (change list page)
#     list_display = ('image', 'label', 'label_name', 'add_date')  

# Register the model with the custom admin class
# admin.site.register(HisData, HisDataAdmin)