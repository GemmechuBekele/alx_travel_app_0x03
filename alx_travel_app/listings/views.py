from django.shortcuts import render

from .tasks import send_booking_confirmation_email

def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    booking = self.get_object()
    user_email = booking.user.email
    booking_details = f'{booking.id} on {booking.date}'

    send_booking_confirmation_email.delay(user_email, booking_details)

    return response

