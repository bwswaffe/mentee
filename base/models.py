from django.db import models

# Create your models here.
class Mentor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    #specializations

    def __str__(self):
        return self.first_name + " " + self.last_name 
    
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    company_type = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name
    
class Specializations(models.Model):
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.specialization
    
