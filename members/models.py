# members/models.py

from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default="Unknown Department")  
    address = models.CharField(max_length=255, default="No address provided")  
    contact_no = models.CharField(max_length=20, null=True, blank=True)
    batch = models.CharField(max_length=255,default='2022-2026')
    insta_id = models.CharField(max_length=255,default='No address provided')
    linkedin_id = models.CharField(max_length=255,default='No address provided')
    github_id = models.CharField(max_length=255,default='No address provided')

    class Meta:
        db_table = 'members_student'  

