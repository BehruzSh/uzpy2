from django.shortcuts import render,redirect
# Create your views here.
from .models import Xaridor,Kiyim
from .forms import KiyimForm
from django.contrib import messages
def index(request):
    return render(request,'index.html',{})
def about(request):
    return render(request,'about.html',{})
def contact(request):
    return render(request,'contact.html',{})
def gallery(request):
    return render(request,'gallery.html',{})
def product(request):
    return render(request,'product.html',{})
def service(request):
    return render(request,'service.html',{})
def xaridor(request):
    kiyim_form=""
    if request.method == "POST":
        kiyim_form = KiyimForm(request.POST)
        if kiyim_form.is_valid():
            kiyim_form.save()
            messages.success(request, ('Your kiyim was successfully added!'))
            return redirect('index')
        else:
            messages.error(request, 'Error saving form')
    data=Kiyim.objects.all()
    return render(request,'xaridor.html',{"kiyim":kiyim_form,'data':data})