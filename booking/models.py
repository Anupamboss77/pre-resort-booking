from django.db import models


class Booking(models.Model):

    ROOM_CHOICES = [
        ('Deluxe Room', 'Deluxe Room'),
        ('Luxury Room', 'Luxury Room'),
        ('Family Room', 'Family Room'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    room_type = models.CharField(
        max_length=50,
        choices=ROOM_CHOICES
    )

    check_in = models.DateField()
    check_out = models.DateField()

    guests = models.IntegerField()

    special_request = models.TextField(
        blank=True,
        null=True
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    booking_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name + " - " + self.room_type