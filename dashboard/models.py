from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    basic_concepts_progress = models.IntegerField(default=0)
    redox_reactions_progress = models.IntegerField(default=0)
    atomic_structure_progress = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s Progress"

    @property
    def total_progress(self):
        return (self.basic_concepts_progress + 
                self.redox_reactions_progress + 
                self.atomic_structure_progress) / 3
