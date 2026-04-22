from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.PositiveIntegerField()
    Email_id=models.EmailField()
    Phone=models.PositiveBigIntegerField()

    def __str__(self):
        return self.Name+ ' ' +self.Email_id    
    

class Profile(models.Model):
    Name=models.CharField(max_length=100)
    Resume=models.FileField(upload_to='media')


class Student(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.PositiveIntegerField()
    Email_id=models.EmailField()
    Phone=models.PositiveBigIntegerField()
    Gender_Choices=[
        ("M",'Male'),
        ("F",'Female'),
        ("O",'Others')
    ]
    Gender=models.CharField(max_length=100,choices=Gender_Choices)

class AddMark(models.Model):
    Sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    Mark=models.IntegerField()
    Grade=models.CharField(max_length=100)