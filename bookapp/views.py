from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

class HomeView(View):
    def get(self,request):
        qs=Book.objects.all()
        con_dic={"records":qs}
        return render(request,'home.html',con_dic)

def InsertInput(request):
    return render(request,'bookinput.html')

class AdminpageView(View):
    def get(self,request):
        qs = Book.objects.all()
        con_dic = {"records": qs}
        return render(request,'admin.html',con_dic)
def Customerpage(request):
    qs = Book.objects.all()
    con_dic = {"records": qs}
    return render(request,'customer.html',con_dic)


def Inser(request):
    b_id=int(request.GET["t1"])
    b_name=request.GET["t2"]
    b_cost=float(request.GET["t3"])
    b_author=request.GET["t4"]
    b_pdate=request.GET["t5"]
    b_qnt=request.GET["t6"]
    b1=Book(bid=b_id,bname=b_name,bcost=b_cost,bauthor=b_author,bpdate=b_pdate,quantity=b_qnt)
    b1.save()
    resp=HttpResponse("product inserted successfully")
    return resp

class DisplayView(View):
    def get(self,request):
        qs=Book.objects.all()
        con_dic={"records":qs}
        return render(request,con_dic)

def DeleteInput(request):
    return render(request,"deleteinput.html")

def Delete(request):
    b_id=int(request.GET["t1"])
    B=Book.objects.filter(bid=b_id)
    B.delete()
    resp = HttpResponse("product deleted successfully")
    return resp

def UpdateInput(request):
    return render(request,"updateinput.html")

def Update(request):
    b_id = int(request.GET["t1"])
    b_name = request.GET["t2"]
    b_cost = float(request.GET["t3"])
    b_author = request.GET["t4"]
    b_pdate = request.GET["t5"]
    b_qnt=request.GET["t6"]
    B=Book.objects.get(bid=b_id)
    B.bname=b_name
    B.bcost=b_cost
    B.bauthor=b_author
    B.bpdate=b_pdate
    B.quantity=b_qnt
    B.save()
    resp = HttpResponse("product updated successfully")
    return resp

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            qs=User.objects.filter(is_staff=True,username=username)
            if qs:
                login(request,user)
                return redirect('adminpage')
            else:
                login(request, user)
                return redirect('customerpage')
    context = {}
    return render(request, 'Login.html', context)

def registerPage(request):
    form = createuserform()
    cust_form = createcustomerform()
    if request.method == 'POST':
        form = createuserform(request.POST)
        cust_form = createcustomerform(request.POST)
        if form.is_valid() and cust_form.is_valid():
            user = form.save()
            customer = cust_form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('login')
    context = {
        'form': form,
        'cust_form': cust_form,
    }
    return render(request, 'register.html', context)

def Aboutus(request):
    return render(request, 'aboutus.html')

def Contactus(request):
    return render(request,'contactus.html')


def logoutPage(request):
    logout(request)
    return redirect('/')


def viewcart(request):
    cust = Customer.objects.filter(user=request.user)
    for c in cust:
        carts = Cart.objects.all()
        for cart in carts:
            if (cart.customer == c):
                context = {
                    'cart': cart
                }
                return render(request, 'viewcart.html', context)
        else:
            return render(request, 'emptycart.html')


def addtocart(request, pk):
    book = Book.objects.get(bid=pk)
    cust = Customer.objects.filter(user=request.user)

    for c in cust:
        carts = Cart.objects.all()
        reqcart = ''
        for cart in carts:
            if (cart.customer == c):
                reqcart = cart
                break
        if (reqcart == ''):
            reqcart = Cart.objects.create(customer=c,)
        reqcart.books.add(book)
    return redirect('customerpage')


def deletecart(request):
    cust = Customer.objects.filter(user=request.user)

    for c in cust:
        carts = Cart.objects.all()
        reqcart = ''
        for cart in carts:
            if (cart.customer == c):
                reqcart = cart
                break
        if (reqcart == ''):
            reqcart = Cart.objects.create(customer=c,)
        reqcart.delete()
    return redirect('viewcart')

def removecart(request, pk):
    book = Book.objects.get(bid=pk)
    cust = Customer.objects.filter(user=request.user)

    for c in cust:
        carts = Cart.objects.all()
        reqcart = ''
        for cart in carts:
            if (cart.customer == c):
                reqcart = cart
                break
        if (reqcart == ''):
            reqcart = Cart.objects.create(customer=c,)
        reqcart.books.remove(book)
    return redirect('viewcart')


