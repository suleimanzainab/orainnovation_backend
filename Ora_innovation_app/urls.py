
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileView
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
# from accounts.views import RegisterAPI
from . import views

urlpatterns = [
    path('new_enterprise/', views.CreateEnterprise, name="Enterprisecreate"),#creation of Enterprise
    path('list_enterprises/', views.Enterprise_list, name="EnterpriseList"),# returning all enterprise
    path('list_Enterprise/<str:id>', views.Getenterprise, name="Enterprise_by_id"),#returning enterprise data
    # path('remove_Agency/<str:uuid>', views.Deleteagency, name="DeleteAgency"),#remove agency
    # path('update_Agency/<str:uuid>', views.Updateagency, name="udpdateAgency"),#UpdateAgency

    #customer urls
    path('createCustomer/', views.create_Customer, name="createCustomer"),#create customer
    path('list_Customers/', views.customer_list, name="CustomerList"),# returning all customer
    path('list_Customer/<str:uuid>', views.Getcustomer, name="CustomerList_by_uuid"),#returning customer list by uuid
    path('update_Customer/<str:uuid>', views.UpdateCustomer, name="udpdateCustomer"),#UpdateCustomer
    # path('delete_Customer/<str:uuid>', views.DeleteCustomer, name="deleteCustomer"),#UpdateCustomer

    # user urls
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),#userprofile

    path('new_category/', views.Createcategory, name="Categorycreate"),#creation of Enterprise
    path('list_categories/', views.Allcategory, name="categoryList"),
    
   #services
    path('new_service/', views.Createservice, name="Servicecreate"),#creation of Enterprise
    path('list_services/', views.Allservice, name="ServiceList"),

    #posts
    path('new_post/', views.Postactivities, name="Servicecreate"),#creation of Enterprise
    path('list_posts/', views.Postactivities_list, name="ServiceList"),
    path('list_postss/', views.Postactivities_list_customer, name="ServiceList"),
    path('get_post/<str:id>', views.GetActivity, name="ServiceList"),
   

   #bookings
    path('new_book/', views.BookforService, name="Bookingcreate"),#creation of Enterprise
    path('list_bookings/', views.AllBookings, name="BookingList"),
    path('get_booking/<str:id>', views.GetActivity, name="booking_by_id"),
    path('update_booking/<str:id>', views.UpdateBooking, name="updateBooking"),
    path('events/',views.AllEvents,name="Events"),
    #orders
    path('new_order/', views.OrderforService, name="Ordercreate"),#creation of Enterprise
    path('list_orders/', views.AllOrders, name="OrdersList"),
   
   #cart
   path('Add_cart/', views.AddtoCart, name="cartcreate"),#creation of Enterprise
   path('list_carts/', views.AllCart, name="OrdersList"),
   path('remove_item/<str:id>', views.DeleteCart, name="removeitem"),

   #notification
    path('new_notification/', views.PostNotification, name="notificationcreate"),#creation of Enterprise

]