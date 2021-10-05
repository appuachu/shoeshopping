from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth




def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:

            messages.info(request,'Invalid credential')
            return redirect('login')

    else:
        return render(request,"login.html")
        # return render(request, "login.html")

def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
    #     user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email,password=password)
    #     user.save();
    #     print("user creared")
    #     return redirect('/')
    # else:
    #     return render(request,"registration.html")


        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info( request,"Username is already exists ")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save();
                print("user creared")
                return redirect('/')

        else:
            print('not created')
            return redirect('register')

    else:
        return render(request,"registration.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

