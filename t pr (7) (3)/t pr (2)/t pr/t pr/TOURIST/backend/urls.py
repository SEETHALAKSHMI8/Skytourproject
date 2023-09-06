from django.urls import path
from backend import views


urlpatterns =[
       path('homepage/',views.homepage,name="homepage"),
       path('categorypage/', views.categorypage, name="categorypage"),
       path('savecategory/', views.savecategory, name="savecategory"),
       path('displaycategory/', views.displaycategory, name="displaycategory"),
       path('editcategory/<int:dataid>/', views.editcategory, name="editcategory"),
       path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
       path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),
       path('productpage/', views.productpage, name="productpage"),
       path('saveproduct/', views.saveproduct, name="saveproduct"),
       path('displayproduct/', views.displayproduct, name="displayproduct"),
       path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
       path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
       path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),

       path('adminloginpage/', views.adminloginpage, name="adminloginpage"),
       path('admin_login/', views.admin_login, name="admin_login"),
       path('admin_logout/', views.admin_logout, name="admin_logout"),

]