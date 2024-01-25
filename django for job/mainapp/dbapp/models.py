from django.db import models

# Create your models here.
class databases(models.Model):
    student_id=models.IntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    grade=models.IntegerField()