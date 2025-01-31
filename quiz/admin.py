from django.contrib import admin
from .models import Quiz, Question, QuizAttempt

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 4

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'chapter', 'time_limit')
    list_filter = ('chapter',)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizAttempt)
