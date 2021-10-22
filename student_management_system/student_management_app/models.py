from django.db import models

# Create your models here.
class Student(models.Model):  
    name = models.CharField(max_length=100)    
    date_of_birth = models.DateField()  
    address = models.TextField()     
    student_phone_number = models.CharField(max_length=10, )
    student_email = models.EmailField()
    guardian_phone_number = models.CharField(max_length=10, )
    guardian_email = models.EmailField()
    uid = models.CharField(max_length=64, unique=True)
  

    def __str__(self):
        return self.name


class MarkList(models.Model):  

    # We could also use a onetoone relation with the student, but I'm assuming we don't have to create a R/S
    # student_uid = models.OneToOneField('Student', to_field='uid',primary_key=True, related_name='student_uid', on_delete=models.SET_NULL)

    student_uid = models.CharField(max_length=64, unique=True)
    student_name = models.CharField(max_length=100)
    # Since we have only one course (i.e Computer Science), for now. 
    # We are putting it as default.
    course_name = models.CharField(max_length=20, default="Computer Science")
    # Year in which exam is conducted, we only have to only store the year not the date.
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    marks_scored_percentage = models.FloatField()


    def __str__(self):
        return self.student_name + " " + self.course_name + " " +  str(self.year) 


class Course(models.Model):
    """
    Might use later
    """
    pass