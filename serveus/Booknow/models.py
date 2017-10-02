from django.db import models

class service_providers(models.Model):
    SPName = models.CharField(max_length=200)
    SPPhone_num = models.CharField(max_length=10)
    SPAddress = models.CharField(max_length=500)
    SPemail = models.CharField(max_length=70)
    SPpassword = models.CharField(max_length=100) # do we need this ?
    SPrating = models.IntegerField(null=True)
    service_offered = models.CharField(max_length=4)
    description = models.CharField(max_length=255)

class service_list(models.Model):
    type = models.CharField(max_length=200)
    service_provider = models.ForeignKey(service_providers)

class customer(models.Model):
    C_Name = models.CharField(max_length=200)
    C_Phone_num = models.CharField(max_length=10)
    C_Address = models.CharField(max_length=500)
    C_email = models.CharField(max_length=70)
    C_password = models.CharField(max_length=100) # lets do user accounts
    C_rating = models.IntegerField(null=True,)

class admin1(models.Model):
    ADName = models.CharField(max_length=200)
    ADemail = models.CharField(max_length=70)
    ADpassword = models.CharField(max_length=100)

class booking(models.Model):
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_added = models.DateField()
    date_tobe_completed = models.DateField()
    final_price = models.FloatField()
    min_price = models.FloatField()
    max_price = models.FloatField()
    category = models.ForeignKey(service_list)
    statusChioses = (('TBA', 'To Be Assigned'),('As', 'Assigned'),('Can','Cancelled'),('C','Completed'))
    status = models.CharField(max_length=4,choices=statusChioses,default='TBA')
    service_provider = models.ForeignKey(service_providers)
    customer = models.ForeignKey(customer)
