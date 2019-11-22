

# Create your models here.

from django.db import models


class Student(models.Model):
    id = models.CharField(max_length=200,primary_key=True )
    name = models.CharField(max_length=200)

class Professor(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)

class Score(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
