from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    is_job_seekers = models.BooleanField(default=True)
    is_employeers = models.BooleanField(default=False)

class JobSeekers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    nid = models.CharField(max_length=20,blank=True,null=True)
    image = models.ImageField(null=True,blank=True)
    area_of_interest = models.CharField(null=True,blank=True,max_length=250)
    resume = models.FileField(upload_to='resume/%y/%m/%d',blank=True)


class Employeers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=30,null=True,blank=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    company_description = models.TextField(null=True,blank=True)
    company_type = models.CharField(max_length=250,blank=True,null=True)
    website_url = models.CharField(max_length=250,blank=True,null=True)
    contact = models.CharField(max_length=250,blank=True,null=True)

class JobPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    job_description = models.TextField(null=True,blank=True)
    job_requirements = models.TextField(null=True,blank=True)
    responsibilities = models.TextField(null=True,blank=True)
    exprience = models.CharField(max_length=10,null=True,blank=True)
    salary = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    benefits = models.TextField(null=True,blank=True)
    job_nature = models.CharField(max_length=200,null=True,blank=True)
