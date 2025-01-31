from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.TextField()
    duration = models.IntegerField(help_text="Duration in months")

    def __str__(self):
        return f"{self.name} - ₹{self.price}/month"

class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = timezone.now() + timedelta(days=30 * self.subscription.duration)
        super().save(*args, **kwargs)

    def is_active(self):
        return self.active and timezone.now() <= self.end_date

    def __str__(self):
        return f"{self.user.username}'s {self.subscription.name} Subscription"
