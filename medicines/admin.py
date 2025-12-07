from django.contrib import admin

# Register your models here.
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'dosage', 'frequency', 'created_at')
    search_fields = ('name', 'owner__username')