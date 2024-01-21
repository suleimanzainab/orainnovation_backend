from django.contrib.auth.models import User, Group
from django.contrib import admin
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
admin.autodiscover()
from . models import Customers, Enterprise ,User , Activities , Categories , Services ,Bookings,Orders , Cart ,Notification
from rest_framework import generics, permissions, serializers
from django.contrib.auth.hashers import make_password, check_password

class Create_customer_Serializers(serializers.Serializer):
     firstName = serializers.CharField(max_length=200)
     lastName = serializers.CharField(max_length=200)
     phone = serializers.CharField(max_length=200)
     email = serializers.CharField(max_length=200)
     username =serializers.CharField(max_length=200)
     password = serializers.CharField(max_length=200)
     def Create_client(self):
          customer = Customers()
          customer.firstName = self.validated_data.get('firstName')
          customer.lastName = self.validated_data.get('lastName')
          customer.phone = self.validated_data.get('phone')
          customer.save()
          user = User()
          user.email = self.validated_data.get('email')
          user.first_name = customer.firstName
          user.last_name = customer.lastName
          user.phoneNumber = customer.phone
          user.username = self.validated_data.get('username')
          user.password = make_password( self.validated_data.get('password'))
          user.c_ref = customer.pk
          user.role = 'customer'
          user.save()
          return customer
class cutomerSerializer(serializers.ModelSerializer):
     class Meta:
        model = Customers
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = '__all__'
# class agencySerializer(serializers.ModelSerializer):
#      class Meta:
#           model = Agency
#           fields ='__all__'
class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'username','role','user_uuid','first_name','last_name','phoneNumber'] 
class EnterpriseSerializer(serializers.ModelSerializer):
     class Meta:
          model =Enterprise
          fields ='__all__'
class ActivitiesSerializer(serializers.ModelSerializer):
     class Meta:
          model =Activities
          fields =['serviceName','postName','servicesImages','descriptions','price']
class ActivitiesSerializers(serializers.ModelSerializer):
     class Meta:
          model =Activities
          fields =['id','serviceName','postName','servicesImages','descriptions','price','activitycategory','user']
class CategorySerializer(serializers.ModelSerializer):
     class Meta:
          model =Categories
          fields ='__all__' 
class NotifSerializer(serializers.ModelSerializer):
     class Meta:
          model =Notification
          fields ='__all__' 
class ServiceSerializer(serializers.ModelSerializer):
     class Meta:
          model =Services
          fields =['serviceName','category','description'] 
class ServiceSerializers(serializers.ModelSerializer):
     class Meta:
          model =Services
          fields ='__all__'  
class OrderSerializers(serializers.ModelSerializer):
     class Meta:
          model =Orders
          fields =['orderType','service','activityUser']
class OrdersSerializer(serializers.ModelSerializer):
     class Meta:
          model =Orders
          fields ='__all__'  
class CartSerializer(serializers.ModelSerializer):
     class Meta:
          model =Cart
          fields =['service','activity','cost','quantity','postName','price'] 
class CartSerializers(serializers.ModelSerializer):
     class Meta:
          model =Cart
          fields =['id','service','serviceName','activity','cost','quantity','postName','price','servicesImages','user']  
class BookSerializer(serializers.ModelSerializer):
     class Meta:
          model =Bookings
          fields =['customerName','customerPhonenumber','dateofBooking','service','activityUser','postName']   
class Bookstaus_update_Serializers(serializers.ModelSerializer):
     class Meta:
          model =Bookings
          fields =['status'] 
class BookingEventSerializer(serializers.Serializer):
     id = serializers.IntegerField()
     postName =serializers.CharField()
     user = serializers.CharField()
     dateofBooking =serializers.CharField()
class Create_Enterprise_Serializers(serializers.Serializer):
     company = serializers.CharField(max_length=200)
     c_email = serializers.CharField(max_length=200)
     c_phoneNumber = serializers.CharField(max_length=200)
     username =serializers.CharField(max_length=200)
     password = serializers.CharField(max_length=200)
     def Create_enterprise(self):
          enterprise = Enterprise()
          enterprise.company = self.validated_data.get('company')
          enterprise.c_email = self.validated_data.get('c_email')
          enterprise.c_phoneNumber = self.validated_data.get('c_phoneNumber')
          enterprise.save()
          user = User()
          user.email = enterprise.c_email
          user.username = self.validated_data.get('username')
          user.password = make_password( self.validated_data.get('password'))
          user.referenceId =enterprise.pk
          user.referenceName = enterprise.company
          user.role = 'enterprise'
          user.save()
          return enterprise
# class TravelsSerializer(serializers.ModelSerializer):
#      class Meta:
#           model = Travels
#           fields ='__all__'
# class BusSerializer(serializers.ModelSerializer):
#     class Meta:
#           model = Bus
#           fields =['travels']
# class seatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bus
#         fields = ['nbr_of_seats']
# class TicketSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Tickets
#         fields = '__all__'
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Customize token to add user name
    in encoding.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

#     def validate(self, attrs):
#         data = super().validate(attrs)
#         data['name'] = self.Customers.firstName
#         return data