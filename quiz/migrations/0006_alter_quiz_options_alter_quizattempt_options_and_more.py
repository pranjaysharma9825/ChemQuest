# Generated by Django 5.1.5 on 2025-01-23 07:20

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_question_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AlterModelOptions(
            name='quizattempt',
            options={},
        ),
        migrations.AddField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.TextField(default='Test your chemistry knowledge with this quiz.'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='chapter',
            field=models.CharField(choices=[('basic', 'Basic Concepts of Chemistry'), ('redox', 'Redox Reactions'), ('atom', 'Structure of Atom')], default='basic', max_length=20),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='time_limit',
            field=models.IntegerField(default=30, help_text='Time limit in minutes'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(default='Chemistry Quiz', max_length=200),
        ),
        migrations.AlterField(
            model_name='quizattempt',
            name='score',
            field=models.FloatField(),
        ),
    ]
