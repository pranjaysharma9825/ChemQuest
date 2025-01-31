from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    specialization = models.CharField(max_length=100)
    jee_percentile = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    jee_chemistry_rank = models.IntegerField(null=True, blank=True)
    experience = models.IntegerField()
    bio = models.TextField()
    qualifications = models.TextField(default='', blank=True)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name if self.name else self.user.get_full_name()

    class Meta:
        ordering = ['name']

class MentorRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor_requests')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='requests')
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} -> {self.mentor.user.username}"
