from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mentor, MentorRequest

# Create your views here.

@login_required
def mentor_list(request):
    print("Debug: Mentor list view is being called!")  # Debug print
    mentors = Mentor.objects.all()
    print(f"Debug: Found {mentors.count()} mentors")  # Debug print
    return render(request, 'mentors/mentor_list.html', {'mentors': mentors})

@login_required
def mentor_detail(request, mentor_id):
    mentor = get_object_or_404(Mentor, id=mentor_id)
    return render(request, 'mentors/mentor_detail.html', {'mentor': mentor})

@login_required
def request_mentor(request, mentor_id):
    mentor = get_object_or_404(Mentor, id=mentor_id)
    
    # Check if there's already a pending request
    existing_request = MentorRequest.objects.filter(
        student=request.user,
        mentor=mentor,
        status='pending'
    ).exists()
    
    if existing_request:
        messages.warning(request, 'You already have a pending request with this mentor.')
        return redirect('mentor_detail', mentor_id=mentor_id)
    
    if request.method == 'POST':
        message = request.POST.get('message', '')
        MentorRequest.objects.create(
            student=request.user,
            mentor=mentor,
            message=message
        )
        messages.success(request, 'Your request has been sent to the mentor.')
        return redirect('mentors:mentor_list')
    
    return render(request, 'mentors/request_mentor.html', {'mentor': mentor})
