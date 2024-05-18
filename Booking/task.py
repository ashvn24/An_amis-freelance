from .models import Book, Past_booking
from celery import shared_task
from django.utils import timezone

@shared_task
def del_prev_book():
    today = timezone.now().date()

    past_bookings = Book.objects.filter(date__lt=today)
    
    for booking in past_bookings:
        past = Past_booking.objects.create(user = booking.user,
                                    time = booking.time,
                                    date = booking.date,
                                    Phone = booking.Phone,
                                    Name = booking.Name)
        
        past.save()
        
    Book.objects.filter(date__lt=today).delete()