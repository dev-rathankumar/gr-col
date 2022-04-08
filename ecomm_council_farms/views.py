from multiprocessing import context
from django.shortcuts import render
from store.models import Product
from django.views.generic import TemplateView

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products, 
    }
    return render(request,'home.html', context)


class AboutPage(TemplateView):  # new
    template_name = "about_us.html"
