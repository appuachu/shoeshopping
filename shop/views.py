from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.

from .models import *
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.db.models import Q

# from .models import product,collections,categ
# Create your views here.
def shop(request,c_slug=None):
    c_page=None
    prodt=None
    if c_page!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=product.objects.filter(category=c_page,available=True)
    else:

     prodt = product.objects.all()

     ct = categ.objects.all()

     obt=collections.objects.all()
    return render(request,"index.html",{'prodt':prodt,'obt':obt,'ct':ct})


class shopdetails(DetailView):
    model = product
    template_name = 'details.html'
    context_object_name = 'i'

def searching(request):
    prodt=None
    query=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        prodt=product.objects.all().filter(Q(slug__contains=query)|Q(disc__contains=query)|Q(price__contains=query))
    return render(request,"search.html",{'qr':query,'prodt':prodt})

class cartview(DetailView):

    model = product
    template_name = 'cart.html'
    context_object_name = 'i'

def orderview(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        address = request.POST['address']
        email = request.POST['email']
        mobile = request.POST['mobile']
        state = request.POST['state']
        city = request.POST['city']
        zip = request.POST['zip']
        s = placeorder(firstname=firstname, address=address, email=email, mobile=mobile, city=city, state=state,
                       zip=zip)
        s.save()
        return redirect('/')

    return render(request,"order.html")


