from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, Question, QuizAttempt
from dashboard.models import UserProgress

# Create your views here.

@login_required
def quiz_list(request):
    # Get user's completed quizzes
    completed_quizzes = QuizAttempt.objects.filter(user=request.user).values_list('quiz_id', flat=True)
    
    # Get quizzes by chapter
    basic_quizzes = Quiz.objects.filter(chapter='basic')
    redox_quizzes = Quiz.objects.filter(chapter='redox')
    atomic_quizzes = Quiz.objects.filter(chapter='atom')
    
    # Add is_completed flag to each quiz
    for quiz in basic_quizzes:
        quiz.is_completed = quiz.id in completed_quizzes
    for quiz in redox_quizzes:
        quiz.is_completed = quiz.id in completed_quizzes
    for quiz in atomic_quizzes:
        quiz.is_completed = quiz.id in completed_quizzes
    
    return render(request, 'quiz/quiz_list.html', {
        'basic_quizzes': basic_quizzes,
        'redox_quizzes': redox_quizzes,
        'atomic_quizzes': atomic_quizzes,
    })

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    
    if request.method == 'POST':
        score = 0
        attempted_questions = 0
        
        for question in questions:
            answer = request.POST.get(f'q{question.id}')
            if answer:  # Only count attempted questions
                attempted_questions += 1
                if answer == question.correct_answer:
                    score += 1
        
        # Calculate percentage score based on attempted questions
        if attempted_questions > 0:
            percentage_score = (score / attempted_questions) * 100
        else:
            percentage_score = 0
        
        # Create quiz attempt record
        QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=percentage_score
        )
        
        # Update user progress
        progress = UserProgress.objects.get_or_create(user=request.user)[0]
        progress_increment = 20 if percentage_score >= 60 else 10
        
        if quiz.chapter == 'basic':
            progress.basic_concepts_progress = min(100, progress.basic_concepts_progress + progress_increment)
        elif quiz.chapter == 'redox':
            progress.redox_reactions_progress = min(100, progress.redox_reactions_progress + progress_increment)
        elif quiz.chapter == 'atom':
            progress.atomic_structure_progress = min(100, progress.atomic_structure_progress + progress_increment)
        progress.save()
        
        messages.success(request, f'Quiz completed! Your score: {percentage_score:.1f}%')
        return redirect('quiz_results', quiz_id=quiz.id)
    
    return render(request, 'quiz/take_quiz.html', {
        'quiz': quiz,
        'questions': questions,
    })

@login_required
def quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    attempt = QuizAttempt.objects.filter(user=request.user, quiz=quiz).latest('date_attempted')
    
    return render(request, 'quiz/quiz_results.html', {
        'quiz': quiz,
        'attempt': attempt,
    })
