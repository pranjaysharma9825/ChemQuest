from django.contrib import admin
from .models import Mentor, MentorRequest

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'experience', 'availability']
    search_fields = ['name', 'specialization']
    list_filter = ['availability', 'specialization']

@admin.register(MentorRequest)
class MentorRequestAdmin(admin.ModelAdmin):
    list_display = ['student', 'mentor', 'status', 'date_requested']
