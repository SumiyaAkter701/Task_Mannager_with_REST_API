from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE = (
        ('Admin','Admin'),('User','User'),('Staff','Staff'),
    )
    GENDER=(
        ('Male','Male'), ('Female','Female'),
    )
    BLOOD_GROUP=(
        ('A+','A+'),('A-','A-'),('AB+','AB+'),('AB-','AB-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),
    )

    phone_number= models.CharField(max_length=15,null=True,blank=True)
    date_of_birth = models.DateField(blank =True, null=True)
    address= models.CharField(max_length=200, null=True, blank=True)
    user_type= models.CharField(choices=USER_TYPE,max_length=30, null=True, blank=True)
    gender= models.CharField(choices=GENDER,max_length=10, null=True, blank=True)
    blood_group= models.CharField(choices=BLOOD_GROUP,max_length=5, null=True, blank=True)
    bio= models.CharField(max_length=300, null=True, blank=True)
    image= models.ImageField(upload_to='profile_pic',null=True, blank=True)
    
    otp = models.CharField(max_length=6, blank=True, null=True) 
    
    def __str__(self):
        return self.username 
    
