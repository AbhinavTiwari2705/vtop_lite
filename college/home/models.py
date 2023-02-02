from django.db import models

# Create your models here.




class Student(models.Model):
    s_name=models.CharField(max_length=100)
    s_current_sem=models.CharField(max_length=100)
    s_address=models.CharField(max_length=100)
    s_branch=models.CharField(max_length=100)
    s_email=models.EmailField(max_length=100)


class Droupout(models.Model) :
    s_name=models.CharField(max_length=100)
    s_email=models.EmailField(max_length=100)