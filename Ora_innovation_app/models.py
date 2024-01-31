from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import datetime
from django.contrib.postgres.fields import ArrayField
# Create your models here.


def wrapper(instance, filename):
    new_filename = str(datetime.datetime.now()).split(
        '.')[0]+'__'+filename
    return 'servicesImages/'+new_filename
class User(AbstractUser):
  user_uuid = models.UUIDField(
         default = uuid.uuid4,
         editable = False)
  username = models.CharField(max_length=200,unique=True)
  email = models.EmailField(
      verbose_name='Email',
      max_length=255
  )
  password = models.CharField(max_length=200)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  phoneNumber = models.CharField(max_length=200)
  c_ref = models.CharField(max_length=200, blank=True)
  referenceId = models.CharField(max_length=20, blank=True)
  referenceName = models.CharField(max_length=200, blank=True)
  role = models.CharField(max_length=200, blank=True)


  USERNAME_FIELD = 'username'
 
  class Meta:
     db_table = 'Users'
class Customers(models.Model):
   customer_uuid = models.UUIDField(
         default = uuid.uuid4,
         editable = False)
   firstName = models.CharField(max_length=200)
   lastName = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   class Meta:
     db_table = 'Customers'
class Enterprise(models.Model):
   company = models.CharField(max_length=200)
   c_email = models.CharField(max_length=100)
   c_phoneNumber = models.CharField(max_length=200)

   class Meta:
     db_table = 'Enterprise'
class Categories(models.Model):
   category_uuid = models.UUIDField(
         default = uuid.uuid4,
         editable = False)
   categoryName = models.CharField(max_length=200)
   
   class Meta:
     db_table = 'Categories'
class Services(models.Model):
   serviceName = models.CharField(max_length=200)
   category = models.ForeignKey(Categories,null=True,on_delete=models.CASCADE)
   categoryName = models.CharField(max_length=200)
   description = models.CharField(max_length=200)

   class Meta:
     db_table = 'Services'
class Activities(models.Model):
   serviceName = models.ForeignKey(Services, null=True,on_delete=models.CASCADE)
   activitycategory = models.CharField(max_length=200)
   postName = models.CharField(max_length=200)
   servicesImages = models.ImageField(upload_to=wrapper, null=True, default=None)
   descriptions = models.CharField(max_length=200)
   price = models.FloatField()
   user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
   

   class Meta:
     db_table = 'Activities'


class Bookings(models.Model):
   service = models.ForeignKey(Services, null=True,on_delete=models.CASCADE)
   serviceName = models.CharField(max_length=200)
   activityUser = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
   customerName = models.CharField(max_length=200)
   postName = models.CharField(max_length=200)
   customerPhonenumber = models.CharField(max_length=200)
   dateofBooking = models.CharField(max_length=200)
   status = models.CharField(max_length=200)
   user=models.CharField(max_length=200)
   

   class Meta:
     db_table = 'Bookings'

class Orders(models.Model):
   firstName = models.CharField(max_length=200)
   lastname = models.CharField(max_length=200)
   phoneNumber = models.CharField(max_length=200)
   orderType = models.CharField(max_length=200)
   deleveryDateTime = models.CharField()
   pickupDateTime = models.CharField()
   location= models.CharField(max_length=200)
   service = models.ForeignKey(Services, null=True,on_delete=models.CASCADE)
   serviceName = models.CharField(max_length=200)
   activityUser = models.ForeignKey(User, null=True,on_delete=models.CASCADE)

   class Meta:
     db_table = 'Orders'
class Cart(models.Model):
   service = models.ForeignKey(Services, null=True,on_delete=models.CASCADE)
   serviceName = models.CharField(max_length=200)
   servicesImages = models.ImageField(upload_to=wrapper, null=True, default=None)
   postName = models.CharField(max_length=200)
   price = models.FloatField()
   activity=models.ForeignKey(Activities,null=True,on_delete=models.CASCADE)
   quantity = models.FloatField()
   cost = models.FloatField()
   user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
   

   class Meta:
     db_table = 'Cart'


class Notification(models.Model):
   user = models.ForeignKey(User,null=True , on_delete=models.CASCADE)
   message = models.CharField(max_length=256)
   date_of_notifying=models.DateTimeField()
