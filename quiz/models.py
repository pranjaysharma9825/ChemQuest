from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Quiz(models.Model):
    CHAPTER_CHOICES = [
        ('basic', 'Basic Concepts of Chemistry'),
        ('redox', 'Redox Reactions'),
        ('atom', 'Structure of Atom'),
    ]

    title = models.CharField(max_length=200, default="Chemistry Quiz")
    description = models.TextField(default="Test your chemistry knowledge with this quiz.")
    chapter = models.CharField(max_length=20, choices=CHAPTER_CHOICES, default='basic')
    time_limit = models.IntegerField(help_text="Time limit in minutes", default=30)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.quiz.title} - Question {self.id}"

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    date_attempted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.score}%"
