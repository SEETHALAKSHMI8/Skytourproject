from django.shortcuts import render,redirect
from backend.models import categorydb,productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def homepage(req):
    return render (req,"homepage.html")
def categorypage(req):
    return render(req,"category.html")
def savecategory(req):
    if req.method=="POST":
        c=req.POST.get('country')
        d=req.POST.get('description')
        obj=categorydb(country=c,description=d)
        obj.save()
        messages.success(req, "Category Saved Successfully")
        return redirect(categorypage)

def displaycategory(req):
    data=categorydb.objects.all()
    return render(req,"displaycategory.html",{"data":data})
def editcategory(req,dataid):
    data=categorydb.objects.get(id=dataid)
    return render(req,"editcategory.html",{'data':data})
def updatecategory(req,dataid):
    if req.method == "POST":
        c = req.POST.get('country')
        d = req.POST.get('description')
        categorydb.objects.filter(id=dataid).update(country=c,description=d)
        messages.success(req, "Category updated Successfully")
        return redirect(displaycategory)

def deletecategory(req,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "data deleted Successfully")
    return redirect(displaycategory)

def productpage(req):
    data=categorydb.objects.all()
    return render(req,"product.html",{'data':data})

def saveproduct(req):
    if req.method=="POST":
        c=req.POST.get('country')
        p=req.POST.get('place')
        d=req.POST.get('description')
        pr = req.POST.get('price')
        im = req.FILES['image']
        obj=productdb(country=c,place=p, description=d,price=pr,image=im)
        obj.save()
        messages.success(req, " Product Saved Successfully")
        return redirect(productpage)

def displayproduct(req):
    data=productdb.objects.all()
    return render(req,"displayproduct.html",{"data":data})

def editproduct(req,dataid):
    data=categorydb.objects.all()
    products=productdb.objects.get(id=dataid)
    return render(req,"editproduct.html",{"data":data,"products":products})

def updateproduct(req,dataid):
    if req.method=="POST":
        c=req.POST.get('country')
        p=req.POST.get('place')
        d = req.POST.get('description')
        pr=req.POST.get('price')
        try:
            im = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).image
        productdb.objects.filter(id=dataid).update(country=c, place=p,description=d, price=pr, image=file)
        messages.success(req, " Product updated Successfully")

        return redirect(displayproduct)

def deleteproduct(req,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "data deleted Successfully")
    return redirect(displayproduct)

def adminloginpage(request):
    return render(request,"adminlogin.html")
def admin_login(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
    if User.objects.filter(username__contains=username_r).exists():
        user=authenticate(username=username_r,password=password_r)
        if user is not None:
            login(request,user)
            request.session['username']=username_r
            request.session['password']=password_r
            return redirect(homepage)
        else:
            return redirect(adminloginpage)

    else:
        return redirect(adminloginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminloginpage)
