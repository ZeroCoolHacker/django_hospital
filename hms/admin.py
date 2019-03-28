from django.contrib import admin
from hms.models import Patient, Reciept


# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'age', 'gender', )
    list_filter = ('gender',)


@admin.register(Reciept)
class RecieptAdmin(admin.ModelAdmin):
    raw_id_fields = ('patient',)
    search_fields = ('patient__name',)
