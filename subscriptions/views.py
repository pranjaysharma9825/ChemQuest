from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Subscription, UserSubscription

# Create your views here.

@login_required
def subscription_plans(request):
    return render(request, 'subscriptions/subscription_plans.html')

@login_required
def subscribe(request, plan_id):
    # This is a placeholder for subscription logic
    # You would typically integrate with a payment gateway here
    subscription = Subscription.objects.get(id=plan_id)
    
    # Create user subscription
    UserSubscription.objects.create(
        user=request.user,
        subscription=subscription,
        # Add appropriate start and end dates
    )
    
    return redirect('dashboard')
