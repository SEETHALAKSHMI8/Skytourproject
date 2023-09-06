from django.shortcuts import render,redirect
from frontend.models import reservationdb,sign_indb
from backend.models import productdb,categorydb
from django.contrib import messages

# Create your views here.

def webindex(req):
    data=productdb.objects.all()
    cat=categorydb.objects.all()
    return render(req,"webindex.html",{'data':data,'cat':cat})

def aboutpage(req):
    return render (req,"about.html")
def dealspage(req):
    jan=categorydb.objects.all()
    data=productdb.objects.all()
    return render (req,"deals.html",{"data":data,"jan":jan})
def reservationpage(req):
    products=productdb.objects.all()
    return render (req,"reservation.html",{'products':products})
def savereservation(req):
    if req.method == "POST":
        n = req.POST.get('Name')
        m = req.POST.get('mobile')
        g = req.POST.get('Guests')
        d = req.POST.get('date')
        dt = req.POST.get('Destination')
        u = req.POST.get('username')
        obj=reservationdb(Name=n,mobile=m,Guests=g,date=d,Destination=dt,user=u)
        obj.save()
        return redirect(reservationpage)

def bookingdetails(req):
    cart=reservationdb.objects.filter(user=req.session['username'])
    return render(req,"bookingdetails.html",{"cart":cart})
def userloginpage(req):
    return render(req,"loginpage.html")
def user_register(req):
    if req.method=="POST":
        un=req.POST.get('username')
        e=req.POST.get('email')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')
        obj = sign_indb(username=un, email=e, password=p, cpassword=cp)
        obj.save()
        return redirect(userloginpage)
def userlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if sign_indb.objects.filter(username=username_r,password=password_r).exists():

            request.session['username']=username_r
            request.session['password'] = password_r

            return redirect (webindex)
        else:
            return redirect(userloginpage)

    return redirect(userloginpage)

def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(userloginpage)

def searchpage(req):
    if req.method=="POST":
        query=req.POST.get('qry')
        if query:
            results=productdb.objects.filter(country__contains=query)
        else:
            results=[]
        return render(req,"search.html",{'results':results})
def paymentpage(req):
    return render(req,"payment2.html")
def savepayment(req):
    if req.method=="POST":
        cn=req.POST.get('cardnumber')
        my=req.POST.get('monthyear')
        cc=req.POST.get('cvvcode')
        c=req.POST.get('cardname')
        obj = reservationdb(cardnumber=cn, monthyear=my, cvvcode=cc, cardname=c)
        obj.save()

        return redirect(webindex)
