from __future__ import unicode_literals
# from sre_constants import MAX_UNTIL
# from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    email     = models.EmailField(null = True, blank = True)  
    file      = models.FileField(null = True, blank = True)
    # class Meta :
    #     db_table = "student"


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    # class Meta:
    #     db_table="employee"