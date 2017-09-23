from django.db import models

class service_providers(models.Model):
    SP_ID = models.IntegerField(primary_key=True,auto_created=True)
    SPName = models.CharField(max_length=200)
    SPPhone_num = models.CharField(max_length=10)
    SPAddress = models.CharField(max_length=500)
    SPemail = models.CharField(max_length=70)
    SPpassword = models.CharField(max_length=100) # do we need this ?
    SPrating = models.IntegerField(null=True)
    Service = (('PLBM','Plumbing'),('ECTN','Electrician'),) #add services here or import turple from elsewhere
    service_offered = models.CharField(max_length=4, choices=Service)
class customer(models.Model):
    C_ID = models.IntegerField(primary_key=True,auto_created=True)
    C_Name = models.CharField(max_length=200)
    C_Phone_num = models.CharField(max_length=10)
    C_Address = models.CharField(max_length=500)
    C_email = models.CharField(max_length=70)
    C_password = models.CharField(max_length=100) # lets do user accounts
    C_rating = models.IntegerField(null=True,)

class admin(models.Model):
    Admin_ID = models.IntegerField(primary_key=True)
    Employee_num = models.IntegerField(unique=True)
    ADName = models.CharField(max_length=200)
    ADemail = models.CharField(max_length=70)
    ADpassword = models.CharField(max_length=100)

