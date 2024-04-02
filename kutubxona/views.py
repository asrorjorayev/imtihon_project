from django.shortcuts import render
from kitoblar.models import Kitob
def Home_page(request):
    kitoblar=Kitob.objects.order_by('name')
    data={
        "kitoblar":kitoblar
    }
    return render(request,'home.html',context=data)

def about_page(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')