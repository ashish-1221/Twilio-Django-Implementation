from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(null=False,blank=False)
    
    def __str__(self):
        return self.group_name
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="Email",null=True,blank=True,default="email@domain.com")
    first_name = models.CharField(verbose_name="First Name",null=True,blank=True,max_length=50)
    last_name = models.CharField(verbose_name="Last Name",blank=True,max_length=50)
    mobile_no = PhoneNumberField(null=False,blank=False,unique=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    opt_in = models.BooleanField(verbose_name="Receive Text Messages",null=False,blank=False,default=1)
    
    def __str__(self):
        return f"{self.first_name}_{self.last_name}"

# class SmsSupport(models.Model):
#     text_message = models.TextField(verbose_name="SMS Text Field",blank=False,null=False)
#     group = models.ForeignKey(Group,on_delete=models.CASCADE)
    