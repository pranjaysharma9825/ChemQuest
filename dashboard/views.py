from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from quiz.models import QuizAttempt
from .models import UserProgress

# Create your views here.

@login_required
def dashboard(request):
    # Get user progress
    progress = UserProgress.objects.get_or_create(user=request.user)[0]
    
    # Get recent quiz attempts
    quiz_attempts = QuizAttempt.objects.filter(user=request.user).order_by('-date_attempted')[:5]
    
    # Get leaderboard data
    all_progress = UserProgress.objects.all()
    # Sort by total_progress property
    leaderboard = sorted(all_progress, key=lambda x: x.total_progress, reverse=True)[:10]
    
    return render(request, 'dashboard/dashboard.html', {
        'progress': progress,
        'quiz_attempts': quiz_attempts,
        'leaderboard': leaderboard
    })

@login_required
def periodic_table(request):
    return render(request, 'periodic_table.html')
