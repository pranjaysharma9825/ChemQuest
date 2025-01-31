from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ] 