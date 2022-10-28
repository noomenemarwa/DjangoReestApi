from django.db import models

# Create your models here.

# Depatment Model
class Department(models.Model):
    DepartmentId = models.BigAutoField(primary_key =True)
    DepartmentName = models.CharField(max_length=500)

# Employee Model
class Employee(models.Model):
    EmployeeId = models.BigAutoField(primary_key =True)
    EmployeeName = models.CharField(max_length=500)
    Department= models.CharField(max_length=500)
    DateOfJoining = models.DateField(null = True)
    PhotoFileName = models.CharField(max_length=500, null = True)