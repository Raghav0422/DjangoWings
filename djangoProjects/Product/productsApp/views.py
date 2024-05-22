from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict={
        'product1':'TV',
        'product2':'Microwaves',
        'product3':'Oven',
    }
    return render(request,'productsApp/products.html',product_dict)

def toys(request):
    product_dict={
        'product1':'Goku',
        'product2':'Ludo',
        'product3':'Chess',
    }
    return render(request,'productsApp/products.html',product_dict)

def shoes(request):
    product_dict={
        'product1':'Nike',
        'product2':'Adidas',
        'product3':'Puma',
    }
    return render(request,'productsApp/products.html',product_dict)

def index(request):
    return render(request,'productsApp/products.html')