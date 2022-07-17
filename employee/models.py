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



class StudentForeign(models.Model):
    studid = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    class Meta:
        db_table = "StudentForeign"


class SubjectForeign(models.Model):
    Subid = models.IntegerField(primary_key=True)
    SubjectName = models.CharField(max_length=100)
    class Meta:
        db_table = "SubjectForeign"

class MarkForeign(models.Model):
    Markid = models.IntegerField(primary_key=True)
    Studid = models.ForeignKey(StudentForeign, to_field='studid',on_delete=models.CASCADE)
    Subid = models.ForeignKey(SubjectForeign, to_field='Subid',on_delete=models.CASCADE)
    Mark = models.IntegerField()
    class Meta:
        db_table = "MarkForeign"