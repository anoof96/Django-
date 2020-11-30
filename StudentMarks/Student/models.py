from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=256)
    standard = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length = 1, choices = [('F', 'Female'), ('M', 'Male')])
    marks = models.CharField(max_length=3)

    def __str__(self):
        return self.name
