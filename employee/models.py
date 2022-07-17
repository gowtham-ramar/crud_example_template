from django.db import models

# Create your models here.
from django.db import models
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"


class Student(models.Model):
    studid = models.IntegerField()
    Name = models.CharField(max_length=100)
    class Meta:
        db_table = "Student"


class Subject(models.Model):
    Subid = models.IntegerField()
    SubjectName = models.CharField(max_length=100)
    class Meta:
        db_table = "Subject"

class Mark(models.Model):
    Markid = models.IntegerField()
    Studid = models.IntegerField()
    Subid = models.IntegerField()
    Mark = models.CharField(max_length=100)
    class Meta:
        db_table = "Mark"