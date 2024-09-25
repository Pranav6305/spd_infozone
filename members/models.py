# members/models.py

from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default="Unknown Department")  # Add a default value here
    address = models.CharField(max_length=255, default="No address provided")  # Keep your previous default
    contact_no = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
