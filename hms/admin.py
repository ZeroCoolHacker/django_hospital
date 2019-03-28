from django.contrib import admin
from hms.models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'age', 'gender', )
    list_filter = ('gender',)