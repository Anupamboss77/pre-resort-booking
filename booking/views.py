from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from datetime import datetime


ROOM_PRICES = {
    "Deluxe Room": 2500,
    "Luxury Room": 4000,
    "Family Room": 5000,
}


def home(request):
    return render(request, "home.html")


def rooms(request):
    return render(request, "rooms.html")


def booking_form(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        room_type = request.POST.get("room_type")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        guests = request.POST.get("guests") 

        if not name or not email or not phone or not room_type or not guests:
            messages.error(request, "Please fill all required fields.")
            return render(request, "booking.html")

        price = ROOM_PRICES.get(room_type, 0)

        booking = Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            room_type=room_type,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            total_price=price

        )

        return redirect("confirmation", booking_id=booking.id)

    return render(request, "booking.html")


def confirmation(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)

    return render(
        request,
        "confirmation.html",
        {"booking": booking}
    )