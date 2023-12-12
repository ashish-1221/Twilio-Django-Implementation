from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(null=False,blank=False)
    
    def __str__(self):
        return self.group_name
    
class User(models.Model):
    email = models.EmailField(verbose_name="Email",null=False,blank=False,primary_key=True)
    first_name = models.CharField(verbose_name="First Name",null=False,blank=False,max_length=50)
    last_name = models.CharField(verbose_name="Last Name",blank=True,max_length=50)
    mobile_no = PhoneNumberField(null=False,blank=False,unique=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"