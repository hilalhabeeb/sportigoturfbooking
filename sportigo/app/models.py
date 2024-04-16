from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models




class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class Usertable(AbstractUser):
    # Custom fields for your user model
    username = models.CharField(max_length=20, blank=True, null=True, unique=True)
    role = models.CharField(max_length=25, default="normal_user")
    email = models.EmailField(primary_key=True, unique=True)  # Email as unique USERNAME_FIELD
    dob = models.DateField(default='2000-01-01')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Custom User Manager
    objects = CustomUserManager()

    # Additional fields and methods for your custom user model if needed

    def __str__(self):
        return self.email
        
    


class TurfProvider(models.Model):
    venue_name = models.CharField(max_length=255)
    email = models.EmailField(primary_key=True, unique=True)
    contact_number = models.CharField(max_length=15)
    document = models.FileField(upload_to='documents/')
    sports_type = models.CharField(
        max_length=10,
        choices=[('football', 'Football'), ('cricket', 'Cricket')]
    )
    address = models.TextField()
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False) 
    random_password = models.CharField(max_length=20, null=True, blank=True)
    password_updated = models.BooleanField(default=False)


    def __str__(self):
        return self.venue_name
    
from django.db import models

class ClubUser(models.Model):
    club_id = models.CharField(max_length=50, unique=True, default='123') 
    club_name = models.CharField(max_length=255)
    email = models.EmailField(primary_key=True, unique=True)
    contact_number = models.CharField(max_length=15)
    document = models.FileField(upload_to='club_documents/')
    address = models.TextField()
    is_active = models.BooleanField(default=False) 
    random_password = models.CharField(max_length=20, null=True, blank=True)
    password_updated = models.BooleanField(default=False)

    def __str__(self):
        return self.club_name





class TurfListing(models.Model):
    turf_provider = models.ForeignKey(TurfProvider, on_delete=models.CASCADE)
    turf_name = models.CharField(max_length=255)
    sports_type = models.CharField(
        max_length=10,
        choices=[('football', 'Football'), ('cricket', 'Cricket')]
    )
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    available_from = models.TimeField()
    available_to = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.turf_name

class TurfImage(models.Model):
    turf_listing = models.ForeignKey(TurfListing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='turf_images/')

    def __str__(self):
        return f"Image for {self.turf_listing.turf_name}"
    

class Booking(models.Model):
    user = models.ForeignKey(Usertable, on_delete=models.CASCADE, related_name='bookings')
    turf_listing = models.ForeignKey(TurfListing, on_delete=models.CASCADE)
    turf_provider = models.ForeignKey(TurfProvider, on_delete=models.CASCADE)
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.turf_listing.turf_name} by {self.user.email}"
    
class ClubBooking(models.Model):
    user = models.ForeignKey(ClubUser, on_delete=models.CASCADE, related_name='club_bookings')
    turf_listing = models.ForeignKey(TurfListing, on_delete=models.CASCADE)
    turf_provider = models.ForeignKey(TurfProvider, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Club Booking for {self.turf_listing.turf_name} by {self.user.email}"
    

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question