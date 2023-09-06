from django.urls import path
from frontend import views

urlpatterns =[
     path('webindex/',views.webindex,name="webindex"),
     path('aboutpage/', views.aboutpage, name="aboutpage"),
     path('dealspage/', views.dealspage, name="dealspage"),
     path('reservationpage/', views.reservationpage, name="reservationpage"),
     path('savereservation/', views.savereservation, name="savereservation"),
     path('bookingdetails/', views.bookingdetails, name="bookingdetails"),
     path('userloginpage/', views.userloginpage, name="userloginpage"),
     path('user_register/', views.user_register, name="user_register"),
     path('userlogin/', views.userlogin, name="userlogin"),
     path('userlogout/', views.userlogout, name="userlogout"),
     path('searchpage/', views.searchpage, name="searchpage"),
     path('paymentpage/', views.paymentpage, name="paymentpage"),
     path('savepayment/', views.savepayment, name="savepayment")

]


