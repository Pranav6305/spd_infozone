# Generated by Django 5.0.7 on 2024-09-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll_number',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='No address provided', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='contact_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default='Unknown Department', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(default=1),
        ),
    ]
