from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from .models import product,contact,orders,orderupdate,signup,user_exist
import json


# Create your views here.

users=user_exist()
users.user=False
# users.user=False #This condition simply detect the existence of user, whether it is login or not
def index(request):
    # print(users.user)
    if request.method=="POST":
        name1=request.POST.get('u_name','')
        name2=request.POST.get('self_name','')
        if len(name1)!=0:
            name=name1
        elif len(name1)==0:
            name=name2
        print("name is post=========================",name)
        if (len(name)==0):
            users.user=False  # purpose fully doing true ################################################ make sure it should be false
        elif(len(name)!=0):
            users.user=True  
   
        print(users.user)
        allprods=[]
        categories=product.objects.values('category')

        cats={item['category'] for item in categories}
        for cat in cats:
            prod=product.objects.filter(category=cat)
            allprods.append(prod)
        params={'allprods':allprods,'user_name':name,'user_exist':users}
        return render(request,'shop/index.html',params)
#########################################################################################################3   
    if request.method=="GET":
        name1=request.GET.get('u_name','')
        name2=request.GET.get('self_name','')
        if len(name1)!=0:
            name=name1
        elif len(name1)==0:
            name=name2
        print("name is get=========================",name)
        if (len(name)==0):
            users.user=False  # purpose fully doing true ################################################ make sure it should be false
        elif(len(name)!=0):
            users.user=True  
   
        print(users.user)
        allprods=[]
        categories=product.objects.values('category')

        cats={item['category'] for item in categories}
        for cat in cats:
            prod=product.objects.filter(category=cat)
            allprods.append(prod)
        params={'allprods':allprods,'user_name':name,'user_exist':users}
        return render(request,'shop/index.html',params)
    return render(request,'shop/index.html',params)
##############################################################################
    # allprods=[]
    # categories=product.objects.values('category')
    # cats={item['category'] for item in categories}
    # for cat in cats:
    #     prod=product.objects.filter(category=cat)
    #     allprods.append(prod)
    # params={'allprods':allprods,'user_exist':users}
    # return render(request,'shop/index.html',params)
        

def searchMatch(query,item):
    if query.lower() in item.description.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False
def search(request):
    query=request.GET.get('search')
    allprods=[]
    catprods=product.objects.values('category')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prodtemp=product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query ,item)]
        if len(prod)!=0:
            allprods.append(prod)

    params={'allprods':allprods}
    return render(request,'shop/search.html',params)

def prod_category(request):
    if request.method=="GET":
        product_category=request.GET.get('category_name','')
        prod=product.objects.filter(category=product_category)
    return render(request,'shop/category.html',{'category_product':prod,'category_checkout':users})


def about(request):
    return render(request,'shop/about.html')


def contact_data(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        query=request.POST.get('querytype','')
        query_desc=request.POST.get('query_desc','')
        feedback=request.POST.get('feedback','')

        contacts=contact(name=name,email=email,contact_no=phone,query_type=query,query_desc=query_desc,feedback=feedback)
        contacts.save()
    return render(request,'shop/contact.html')


def tracker(request):
    if request.method=="POST":
        orderid=request.POST.get('orderid','')
        email=request.POST.get('email','') 
        try:
            order=orders.objects.filter(order_id=orderid,email=email)
            if len(order)>0:
                update=orderupdate.objects.filter(order_id=orderid)  
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'shop/tracker.html')




def product_view(request,myid):
    #Fetch product according to ID
    prods=product.objects.filter(id=myid)
    print("=======================",prods)
    return render(request,'shop/product_view.html',{'product':prods[0]})


def checkout(request):
    if users.user==True:
        print("user can checkout!")
    elif users.user==False:
        print("user cannot checkout!")

    if request.method=="POST":
        items_json=request.POST.get('itemsJson','')
        amount=request.POST.get('amount','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','') + " " + request.POST.get('address2',' ')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip','')
        phone=request.POST.get('phone','')

        order=orders(items_json=items_json,amount=amount,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()

        update=orderupdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        thank=True
        id=update.order_id   
        # params={'thank':thank,'id':id,'checkout':users.user}
        # return render(request,'shop/checkout.html',params)     
        return render(request, 'shop/paypal.html',{'checkout':users,'id':id,'amount':amount})
    return render(request, 'shop/checkout.html',{'checkout':users})


#Only for Redirection to login page, when it firstly click on click button
def login(request):
    return render(request,'shop/login.html')


def sign_up(request):
    if request.method=="POST":
        name=request.POST.get('signup_fullname','')
        email=request.POST.get('signup_email','')
        password=request.POST.get('signup_password','')
        if(len(name)!=0 and len(email)!=0 and len(password)!=0):
            sign=signup(user_name=name,user_email=email,user_password=password)
            sign.save()
            return render(request,'shop/login.html')
        else:           
            return render(request,'shop/login.html')
    return render(request,'shop/login.html')


def logging(request):

    if request.method=="POST":
        email=request.POST.get('login_email','')
        password=request.POST.get('login_password','')
        print("data are here===",email,password)
        if email=="admin" and password=="123":
            return redirect('http://127.0.0.1:8000/admin/')
        
        elif len(email)!=0 and len(password)!=0:
            user_data=signup.objects.all()
            user_name=[x.user_name for x in user_data]
            user_emails=[x.user_email for x in user_data]
            user_passwords=[x.user_password for x in user_data]
            
            # if len(user_emails)>0 and len(user_passwords)>0:
            if ((email in user_emails) and (password in user_passwords)):
                user_index=0    
                for x in user_emails:
                    if x==email:
                        user_index=user_emails.index(email)
                        break
                # return render(request,'shop/index.html')
                # params={"user_name":user_name[user_index]}
                # return render(request,'shop/index.html',{'user_name':user_name[user_index].capitalize})
                return render(request,'index.html',{'user_name':user_name[user_index].capitalize,'login_state':users})
            # return render(request,'index.html',{'user_name':user_name[user_index].capitalize,'login_state':False})
    return render(request,'shop/login.html')


def paypal(request):
    if request.method=="POST":
        import razorpay
        client=razorpay.Client(auth=('rzp_test_6SZ6Lh51v32BP8', 'grj3HWbU9WCKUBQmx2dOs6AA'))
        DATA = {
        "amount": 100,
        "currency": "INR",
        "receipt": "receipt#1",
        "notes": {
            "key1": "value3",
            "key2": "value2"
        }
        }
        client.order.create(data=DATA)
    # if request.method=="POST":
    #     items_json=request.POST.get('itemsJson','')
    #     amount=request.POST.get('amount','')
    #     name=request.POST.get('name','')
    #     email=request.POST.get('email','')
    #     address=request.POST.get('address1','') + " " + request.POST.get('address2',' ')
    #     city=request.POST.get('city','')
    #     state=request.POST.get('state','')
    #     zip_code=request.POST.get('zip','')
    #     phone=request.POST.get('phone','')

    #     order=orders(items_json=items_json,amount=amount,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
    #     order.save()

    #     update=orderupdate(order_id=order.order_id,update_desc="The order has been placed")
    #     update.save()
    #     thank=True
    #     id=update.order_id   
   
    #     return render(request, 'shop/checkout.html')

    return render(request,'shop/paypal.html')






def invoice(request):

    if request.method=="POST":
        cart=request.GET.get('tracker','')
        print("your cart is====================",cart)
    return render(request,'shop/invoice.html',{'user_exist':users})