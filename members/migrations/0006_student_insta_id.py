# Generated by Django 5.0.7 on 2024-10-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_student_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='insta_id',
            field=models.CharField(default='No address provided', max_length=255),
        ),
    ]
