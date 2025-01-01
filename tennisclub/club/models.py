from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


class TennisClubMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="tennisclubmember")
    ROLE_CHOICES = [
        ('member', 'Member'),
        ('admin', 'Admin'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15)
    username = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    joined_date = models.DateTimeField(auto_now_add=True)
    membership_type = models.CharField(
        max_length=50,
        choices=[
            ('Standard', 'Standard'),
            ('Premium', 'Premium'),
            ('VIP', 'VIP'),
        ],
        default='Standard',
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128)  # Store hashed password
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"

    def save(self, *args, **kwargs):
        if self.user:
            # Sync the email with the related User model
            if not self.email:
                self.email = self.user.email  # Set email from User model if not provided
            else:
                self.user.email = self.email  # Update User's email if TennisClubMember's email changes
                self.user.save()
        if not self.username:
            self.username = self.user.username  # Auto-assign username from related User
        super().save(*args, **kwargs)

    # Implement is_authenticated
    def is_authenticated(self):
        return self.is_active

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, password):
        return check_password(password, self.password)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Tennis Club Member"
        verbose_name_plural = "Tennis Club Members"
