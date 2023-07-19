from django.db import models

# Create your models here.
class Data(models.Model):
    Course_Code = models.CharField(max_length=255)
    Course_Title = models.CharField(max_length=255)
    Course_Teacher = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

def __str__(self):
    return self.Course_Code