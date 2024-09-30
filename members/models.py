# members/models.py

from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default="Unknown Department")  # Add a default value here
    address = models.CharField(max_length=255, default="No address provided")  # Keep your previous default
    contact_no = models.CharField(max_length=20, null=True, blank=True)
    batch = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Student(models.Model):
    # roll_no = models.CharField(max_length=255, primary_key=True)  # Explicitly set as primary key
#     name = models.CharField(max_length=255)
#     department = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     contact_no = models.CharField(max_length=15)

    class Meta:
        db_table = 'members_student'  

