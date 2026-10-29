from django.db import models

# Create your models here.

class TurfDb(models.Model):
    turf_name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    sport_type=models.CharField(max_length=50)
    price_per_hour=models.PositiveIntegerField()
    contact=models.CharField(max_length=15)
    availability=models.BooleanField(default=True)

    def __str__(self):
        return self.turf_name

class BookingDb(models.Model):
    customer_name=models.CharField(max_length=50)
    customer_phone=models.CharField(max_length=15)
    turf=models.ForeignKey(TurfDb,on_delete=models.CASCADE)
    booking_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    total_amount=models.PositiveIntegerField()
    booking_status=models.CharField(
        max_length=50,
        choices=[
            ("Pending","Pending"),
            ("Confirmed","Confirmed"),
            ("Cancelled","Cancelled"),
            ("Completed","Completed")
        ],default="Pending"
    )

    def __str__(self):
        return self.customer_name