from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
import stripe
from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404


def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)


def about(request):
     return render(request, 'shop/about.html',)

def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        contacts = Contact(name = name, email = email, phone = phone, desc = desc)
        contacts.save()   
        
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.time_stamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                    return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
             return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def search(request):
   return render(request, 'shop/search.html')

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        print(request)
        itemJson = request.POST.get('itemJson','')
        name = request.POST.get('name','')
        amount = request.POST.get('amount','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip = request.POST.get('zip','')
        phone = request.POST.get('phone','')
        
        order = Orders(items_json = itemJson, name = name, email = email,address=address,city=city,state=state,zip=zip,phone=phone,amount=amount)
        order.save() 
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        print("87")
        try:
            print("97")
            # product = get_object_or_404(Product,pk=id)
            stripe.api_key= settings.STRIPE_SECRET_KEY
            domain_url = "http://127.0.0.1:8000/shop"
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price':'price_1MCjKeSGv7DzXqX4vize7A7p',
                        'quantity':1
                    }
                ],
                mode="subscription",
                success_url=domain_url+"/success",
                cancel_url=domain_url+"/cancle",
            )
            print("111")
            print(checkout_session.url)
            return redirect(checkout_session.url,code=303)
        except Exception as e:
            print("114")
            return e
    print("91")
    return render(request, 'shop/checkout.html')

# @csrf_exempt    
# def payment():
#     print("95")
    
#     try:
#         print("97")
#         # product = get_object_or_404(Product,pk=id)
#         stripe.api_key= settings.STRIPE_SECRET_KEY
#         domain_url = "http://127.0.0.1:8000/shop"
#         checkout_session = stripe.checkout.Session.create(
#             line_items=[
#                 {
#                     'price':'price_1MCjKeSGv7DzXqX4vize7A7p',
#                     'quantity':1
#                 }
#             ],
#             mode="subscription",
#             success_url=domain_url+"/success",
#             cancel_url=domain_url+"/cancle",
#         )
#         print("111")
#         print(checkout_session.url)
#         return redirect(checkout_session.url,code=303)
#     except Exception as e:
#         print("114")
#         return e      
    
def success(request):
    return render(request,"success.html")


def cancle(request):
     return render(request, "cancle.html")
