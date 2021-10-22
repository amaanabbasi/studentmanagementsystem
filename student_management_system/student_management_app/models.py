from django.db import models

# Create your models here.
class Student(models.Model):  
    name = models.CharField(max_length=100, )    
    date_of_birth = models.DateField()  
    address = models.TextField()     
    student_phone_number = models.CharField(max_length=10, )
    student_email = models.EmailField()
    guardian_phone_number = models.CharField(max_length=10, )
    guardian_email = models.EmailField()
    uid = models.CharField(max_length=64, unique=True)
  

    def __str__(self):
        return self.name