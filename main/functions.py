from .models import *

def product_index(chapter, name_list):
    product = Product.objects.filter(chapter=chapter)
    context = {
        name_list: product,
    }
    return context

def product_detail(slug, element):
    product = Product.objects.get(slug=slug)
    characteristic = Characteristic.objects.filter(kitchen=product)
    image = Img.objects.filter(product=product)
    context = {
         element: product,
        "image_list": image,
        "characteristic_list": characteristic,
    }
    return context
