from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    type=models.CharField(max_length=20)




class Employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    address = models.TextField()
    dob= models.CharField(max_length=20)
    pin = models.IntegerField()
    number = models.BigIntegerField()
    email = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    uid = models.ForeignKey(login, on_delete=models.CASCADE)

class companylogin(models.Model):
    cname = models.CharField(max_length=20)
    cregnum= models.IntegerField()
    cadd = models.TextField()
    contact = models.IntegerField()
    website = models.TextField()
    cid = models.ForeignKey(login, on_delete=models.CASCADE)

class addvacancy(models.Model):
    jt= models.CharField(max_length=20)
    vac= models.IntegerField()
    datefrom = models.TextField()
    dateto = models.TextField()
    skills= models.TextField()
    dis = models.TextField()
    cid = models.ForeignKey(companylogin, on_delete=models.CASCADE)

class sendfeed(models.Model):
    jt= models.TextField(max_length=20)
    company = models.ForeignKey(companylogin, on_delete=models.CASCADE)

class jobreq(models.Model):
    expsalary=models.IntegerField()
    cid=models.ForeignKey(companylogin,on_delete=models.CASCADE)
    eid=models.ForeignKey(Employee,on_delete=models.CASCADE)
    cv=models.FileField(upload_to="cv")

