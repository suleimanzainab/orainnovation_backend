from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .models import *
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer,UserSerializer
from django.contrib.auth import get_user_model
import datetime
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import qrcode
import qrcode.image.svg
from qrcode import *
from django.http import HttpResponse
User = get_user_model()
# Create your views here.

@api_view(['POST'])

@permission_classes([AllowAny])
def create_Customer(request):
        customer_serializer_data = Create_customer_Serializers(data=request.data)
        if customer_serializer_data.is_valid():
           serializer =customer_serializer_data.Create_client()
           serial = cutomerSerializer(serializer)
           return Response(serial.data,status=status.HTTP_201_CREATED)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})
@api_view(['GET'])
@permission_classes([IsAdminUser])
def customer_list(request):
    customer = Customers.objects.all()
    serializer = cutomerSerializer(customer,many=True)
    return Response(serializer.data,status=status.HTTP_302_FOUND)

@api_view(['GET'])

@permission_classes([IsAuthenticated])
def Getcustomer(request,uuid):
    customer = Customers.objects.get(customer_uuid=uuid)
    if customer == None:
        return Response('customer not found',status=status.HTTP_404_NOT_FOUND)
    else:
       serializer = cutomerSerializer(customer,many=False)
       return Response(serializer.data,status=status.HTTP_302_FOUND)

@api_view(['PUT'])

@permission_classes([IsAuthenticated])
def UpdateCustomer(request,uuid):
   customer = None
   try:
        customer = Customers.objects.get(customer_uuid=uuid)
   except:
       if customer == None:
           return Response('customer not found',status=status.HTTP_404_NOT_FOUND)
       
   customer.firstName = request.data['firstName']
   customer.phone = request.data['phone']
   customer.lastName = request.data['lastName']
   serializer = cutomerSerializer(instance=customer,data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data,status=status.HTTP_200_OK)
   else:
     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['POST'])

@permission_classes([AllowAny])
def CreateEnterprise(request):
   # enterprise = Enterprise()
        enterprise_serializer_data = Create_Enterprise_Serializers(data=request.data)
        if enterprise_serializer_data.is_valid():
           serializer =enterprise_serializer_data.Create_enterprise()
           serial = EnterpriseSerializer(serializer)
           return Response(serial.data,status=status.HTTP_201_CREATED)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})
@api_view(['GET'])
@permission_classes([IsAdminUser])
def Enterprise_list(request):
    customer = Enterprise.objects.all()
    serializer = EnterpriseSerializer(customer,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET'])

@permission_classes([IsAuthenticated])
def Getenterprise(request,id):
    customer = Enterprise.objects.get(id=id)
    if customer == None:
        return Response('Enterprise not found',status=status.HTTP_404_NOT_FOUND)
    else:
       serializer = EnterpriseSerializer(customer,many=False)
       return Response(serializer.data,status=status.HTTP_200_OK)
class UserProfileView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])

@permission_classes([IsAuthenticated])
def Postactivities(request):
    active = Activities()
    print(Services.objects.get(id=request.data['serviceName']))
    active.serviceName = Services.objects.get(id=request.data['serviceName'])
    active.activitycategory= Services.objects.get(id=request.data['serviceName']).categoryName
    active.postName = request.data['postName']
    active.servicesImages = request.FILES.get('servicesImages')
    active.descriptions = request.data['descriptions']
    active.price = request.data['price']
    active.user = request.user
    serializers = ActivitiesSerializer(instance=active,data=request.data)
    if serializers.is_valid():
       serializers.save()
       return Response(serializers.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])

@permission_classes([IsAuthenticated])
def Postactivities_list(request):
    customer = Activities.objects.get(user = request.user)
    serializer = ActivitiesSerializer(customer,many=True)
    print(serializer.data)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])

@permission_classes([IsAuthenticated])
def Postactivities_list_customer(request):
    customer = Activities.objects.all()
    serializer = ActivitiesSerializers(customer,many=True)
    print(serializer.data)
    data={}
    data=customer
    print(data)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET'])

@permission_classes([IsAuthenticated])
def Postactivities_list(request):
    customer = Activities.objects.filter(user = request.user)
    serializer = ActivitiesSerializer(customer,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])

@permission_classes([IsAuthenticated])
def GetActivity(request,id):
    customer = Activities.objects.filter(user = request.user,id=id)
    data ={}
    serializer = ActivitiesSerializer(customer)
    data = {"s"}
    print(data)
    return Response(data,status=status.HTTP_200_OK)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def Createcategory(request):
    category = Categories()
    category.categoryName = request.data['categoryName']
    serializers = CategorySerializer(instance=category,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAdminUser])
def Allcategory(request):
    category = Categories.objects.all()
    serializers = CategorySerializer(category,many=True)
    return Response(serializers.data,status=status.HTTP_200_OK)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def Createservice(request):
    service = Services()
    service.serviceName = request.data['serviceName']
    cat = Categories.objects.get(id= request.data['category'])
    service.category = Categories.objects.get(id= request.data['category'])
    #print("+++++++++++++",cat)
    service.description = request.data['description']
    #name =cat.categoryName
    service.categoryName =cat.categoryName
    serializers = ServiceSerializer(instance=service,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Allservice(request):
    service = Services.objects.all()
    serializers = ServiceSerializers(service,many=True)
    print(serializers.data)
    return Response(serializers.data,status=status.HTTP_200_OK)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BookforService(request):
    booking = Bookings()
    booking.customerName = request.data['customerName']
    booking.customerPhonenumber = request.data['customerPhonenumber']
    booking.dateofBooking = request.data['dateofBooking']
    booking.service = Services.objects.get(id=request.data['service'])
    serve = Services.objects.get(id=request.data['service'])
    booking.serviceName = serve.serviceName
    booking.user=request.user
    booking.postName = request.data['postName']
    booking.status = 'pending'
    booking.activityUser = User.objects.get(id=request.data['activityUser'])
    serializers = BookSerializer(instance=booking,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllBookings(request):
    booking = Bookings.objects.filter(activityUser=request.User)
    if booking==None:
        return Response('bookings not found',status=status.HTTP_404_NOT_FOUND)
    else:
      serializers = BookSerializer(booking,many=True)
      return Response(serializers.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_Book(request,id):
     booking = Bookings.objects.get(id=id)
     if booking ==None:
         return Response('Booking not found', status=status.HTTP_404_NOT_FOUND)
     else:
         serializers =BookSerializer(booking,many=False)
         return Response(serializers.data,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateBooking(request,id):
    booking = Bookings.objects.get(id=id)
    if booking ==None:
         return Response('Booking not found', status=status.HTTP_404_NOT_FOUND)
    else:
       booking.status ='Approved'
       serializers = Bookstaus_update_Serializers(instance=booking,data=request.data)
       if serializers.is_valid():
           serializers.save()
           return Response(serializers.data,status=status.HTTP_201_CREATED)
       else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


# #order
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def OrderforService(request):
    order = Orders()
    order.firstName =request.user.first_name
    order.lastname =request.user.last_name
    order.phoneNumber=request.user.phoneNumber
    order.orderType = request.data['orderType']
    if (order.orderType == 'pickup'):
        order.pickupDateTime = request.data['pickupDateTime']
        order.deleveryDateTime = "2024-03-12 13:30:09+00"
    else:
        order.deleveryDateTime= request.data['delivaryDateTime']
        order.pickupDateTime ="2024-03-12 13:30:09+00"
    
    order.service=Services.objects.get(id=request.data['service'])
    order.activityUser=User.objects.get(id=request.data['activityUser'])
    order.serviceName =Services.objects.get(id=request.data['service']).serviceName
    serializers = OrderSerializers(instance=order,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllOrders(request):
    orders = Orders.objects.filter(activityUser=request.User)
    if orders==None:
        return Response('orders not found',status=status.HTTP_404_NOT_FOUND)
    else:
      serializers = OrdersSerializer(orders,many=True)
      return Response(serializers.data,status=status.HTTP_200_OK)

#cart

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddtoCart(request):
    cart=Cart()
    cart.service =Services.objects.get(id=request.data['service'])
    cart.serviceName =Services.objects.get(id=request.data['service']).serviceName
    cart.servicesImages = Activities.objects.get(id=request.data['activity']).servicesImages
    cart.postName = request.data['postName']
    cart.price=request.data['price']
    cart.user=request.user
    cart.quantity=request.data['quantity']
    cart.cost=request.data['cost']
    serializers = CartSerializer(instance=cart,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllCart(request):
    cart = Cart.objects.filter(user=request.user)
    if cart==None:
        return Response('cart not found',status=status.HTTP_404_NOT_FOUND)
    else:
      serializers = CartSerializers(cart,many=True)
      print(serializers.data)
      return Response(serializers.data,status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def DeleteCart(request,id):
    cart = Cart.objects.filter(user=request.User,id=id)
    if cart==None:
        return Response('cart not found',status=status.HTTP_404_NOT_FOUND)
    else:
      cart.delete()
      return Response("item removed from cart successfully",status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllEvents(request):
    bookings = Bookings.objects.filter(user=request.user)
    serializers= BookingEventSerializer(bookings,many=True)
    print(serializers.data)
    return Response(serializers.data,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PostNotification(request):
    notification= Notification()
    notification.user= request.data['user']
    notification.message = request.data['message']
    notification.date_of_notifying=request.data['data_of_notifying']
    notification.save()
    return Response(notification,status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Allnotification(request):
    notif=Notification.objects.all()
    serializer =NotifSerializer(notif,many=True)
    return Response(serializer,status=status.HTTP_200_OK)