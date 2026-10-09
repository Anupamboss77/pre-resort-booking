from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'room_type',
        'check_in',
        'check_out',
        'guests',
        'total_price',
        'booking_date'
    )

    list_filter = (
        'room_type',
        'check_in',
        'check_out'
    )

    search_fields = (
        'name',
        'email',
        'phone'
    )