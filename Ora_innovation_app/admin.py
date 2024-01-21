from django.contrib import admin
from .models import User , Services,Activities,Enterprise , Orders ,Bookings, Categories ,Customers,Cart
# Register your models here.
admin.site.register(User)
admin.site.register(Services)
admin.site.register(Activities)
admin.site.register(Enterprise)
admin.site.register(Orders)
admin.site.register(Bookings)
admin.site.register(Categories)
admin.site.register(Customers)
admin.site.register(Cart)
