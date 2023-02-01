from django.db import models

# Create your models here.




class Student(models.Model):
    s_name=models.CharField(max_length=100)
    s_current_sem=models.CharField(max_length=100)
    s_address=models.CharField(max_length=100)
    s_branch=models.CharField(max_length=100)
    s_email=models.EmailField(max_length=100)

    def __str__(self):
        return self.s_name + ' -- '*2 + self.s_current_sem + ' -- '*2 + self.s_address + ' -- '*2 + self.s_branch + ' -- '*2 + self.s_email

