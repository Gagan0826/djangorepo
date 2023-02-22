from django.contrib import admin
from .models import Alumni
# Register your models here.

class AlumniAdmin(admin.ModelAdmin):
    list_display = ('id', 'usn', 'name', 'batch', 'company', 'address', 'PROEmail', 'OFFEmail', 'contact_no', 'designation', 'domain', 'willing_contribution')
admin.site.register(Alumni)