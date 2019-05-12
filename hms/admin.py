from django.contrib import admin
from hms.models import Patient, Reciept
from django.utils.html import mark_safe


# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'age', 'gender', )
    list_filter = ('gender',)


@admin.register(Reciept)
class RecieptAdmin(admin.ModelAdmin):
    readonly_fields = ["headshot_image",]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.reciept.url,
            width=obj.reciept.width,
            height=obj.reciept.height,
            )
    )
    empty_value_display = '--Empty--'


    raw_id_fields = ('patient',)
    search_fields = ('patient__name',)
