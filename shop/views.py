from math import ceil

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from shop.models import Product,Contact


def index(req):
    #product=Product.objects.all()
    #n=len(product)
    #ns=n//4+ceil(n/4-n//4)
    # 1st params={'product':product,"range":range(1,ns),'ns':ns}
    # 2nd allprod=[[product,range(1,ns),ns],[product,range(1,ns),ns]]
    allprod=[]

    search = req.POST.get('search', "")
    catprods=Product.objects.values('catagory','id')
    cats={item["catagory"] for item in catprods}
    for cat in cats:
        prodtemp=Product.objects.filter(catagory=cat)
        prod=[ item for item in prodtemp if search in item.name]
        n=len(prod)
        ns=n//4+ceil(n/4-n//4)
        allprod.append([prod,range(1,ns),ns])
    params={"allprod":allprod}
    return render(req,'shop/index.html',params)

def productView(req,id):


    product=Product.objects.get(id=id)
    return render(req,'shop/product_view.html',{'product':product})

def contact(req):
    if req.method=="POST":
        name=req.POST.get('name','')
        email = req.POST.get('email', '')
        phone = req.POST.get('phone', '')
        desc = req.POST.get('desc', '')
        print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(req,'shop/contact.html')
def about(req):
    return render(req,'shop/about.html')

