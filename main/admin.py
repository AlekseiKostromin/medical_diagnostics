from django.contrib import admin
from main.models import TestCategory, LabTest, Doctor, Booking


@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'time',)
    list_filter = ('name', 'price', 'time',)
    search_fields = ()
    list_per_page = 10


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('specialization', 'price',)
    list_filter = ('specialization',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'timeslot', 'is_booked', 'patient')
    list_filter = ('doctor', 'date', 'timeslot', 'is_booked', 'patient')
    list_editable = ['is_booked']
