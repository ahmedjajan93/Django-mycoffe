from django.shortcuts import render ,get_object_or_404
from .models import Product

# Create your views here.
 
def product(request , prod_id):

    
    context ={
        'pro':get_object_or_404(Product , pk=prod_id)
    }
    return render(request , 'products/product.html',context)
 
def products(request):
    pro = Product.objects.all()
    desc = None
    name = None
    prfrom = None
    prto = None
    cs = None

    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            pro = pro.filter(name__icontains = name)

    if "search-des"in request.GET:
        desc = request.GET["search-des"]
        if desc:
            pro = pro.filter(des__icontains = desc)

    if "searchpricefrom" in request.GET and "searchpriceto" in request.GET:
        prfrom = request.GET["searchpricefrom"]
        prto = request.GET["searchpriceto"]
        if prfrom and prto :
            if prfrom.isdigit() and prto.isdigit():
                pro = pro.filter(price__gte = prfrom , price__lte = prto)

    if "cs" in request.GET:
        cs = request.GET["cs"]
        if not cs :
            cs = "off"

    if "searchname" in request.GET:
         name =request.GET["searchname"]
         if name:
             if cs=='on':
                 pro = pro.filter(name__contains=name)
             else:
                 pro = pro.filter(name__icontains=name)
    
    if "searchdesc" in request.GET:

         desc =request.GET["searchdesc"]
         if desc:
             if cs=='on':
                 pro = pro.filter(des__contains=desc)
             else:
                 pro = pro.filter(des__icontains=desc)


    context = {
        'products': pro
    }
    return render(request,'products/products.html',context)

def search(request):
    return render (request , 'products/search.html')