# Generated by Django 5.0.7 on 2024-10-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_student_insta_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='linkedin_id',
            field=models.CharField(default='No address provided', max_length=255),
        ),
    ]
