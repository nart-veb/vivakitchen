from django.shortcuts import render
from .functions import *
from django.views.generic.base import View
from .models import *


class IndexView(View):
    # главная страница
    def get(self, request):
        slide = Slider.objects.all()
        product_portfolio = Product.objects.filter(portfolio=1)
        product_vip = Product.objects.filter(kitchen="1")
        process = Process.objects.all()
        context = {
            "slide_list": slide,
            "process_list": process,
            "product_portfolio_list": product_portfolio,
            "product_vip_list": product_vip,
        }
        return render(request, 'vivakitchen/index.html', context)



class Portfolio(View):
    # мебель лист
    def get_index(request):
        context = product_index("PORTFOLIO", "product_list")
        context["title"] = "портфолио"
        context["header"] = "портфолио"
        context["description"] = ""
        return render(request, "vivakitchen/portfolio/portfolio_index.html", context)

    def get_detail(request, slug):
        context = product_detail(slug, "product")
        context["title"] = "портфолио"
        context["header"] = "кухня"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_detail.html", context)




class Promotion(View):
    def get(self, request):
        return render(request, 'vivakitchen/promotion.html')

class Buyer(View):
    def get(self, request):
        process = Process.objects.all()
        context = {
            "process_list": process,
        }
        return render(request, 'vivakitchen/buyer.html', context)

class Contact(View):
    def get(self, request):
        return render(request, 'vivakitchen/contact.html')

class About(View):
    def get(self, request):
        return render(request, 'vivakitchen/about.html')


class ListIndex(View):
    # мебель лист
    def get_index(request, slug, name_list=None):
        if Nav.objects.filter(slug=slug):
            id_slug = Nav.objects.get(slug=slug)
            if Page.objects.filter(nav=id_slug):
                page = Page.objects.get(nav=id_slug)
                image = ImgPage.objects.filter(page=page)
                return render(request, "vivakitchen/page/page_detail.html", {"page": page, "image_list": image})
            elif Product.objects.filter(nav=id_slug):
                product = Product.objects.filter(nav=id_slug)
                context = {"product_list": product, "name_list": product, "title": id_slug, "header": id_slug,
                           "description": ""}
                return render(request, "vivakitchen/product/product_index.html", context)
            else:
                return render(request, "vivakitchen/inactive.html", {'nav': id_slug.name})

        elif ShowNav.objects.filter(slug=slug):
            id_slug = ShowNav.objects.get(slug=slug)
            if Page.objects.filter(show_nav=id_slug):
                page = Page.objects.get(show_nav=id_slug)
                image = ImgPage.objects.filter(page=page)
                return render(request, "vivakitchen/page/page_detail.html", {"page": page, "image_list": image})
            elif Product.objects.filter(show_nav=id_slug):
                product = Product.objects.filter(show_nav=id_slug)
                context = {"product_list": product, "name_list": product, "title": id_slug, "header": id_slug,
                           "description": ""}
                return render(request, "vivakitchen/product/product_index.html", context)
            else:
                return render(request, "vivakitchen/inactive.html", {'nav': id_slug.name})
        else:
            return render(request, "vivakitchen/none.html")


    def get_detail(request, nav, slug,):
        product = Product.objects.get(slug=slug)
        if (product.nav is None and product.show_nav.slug == nav) or (product.show_nav is None and product.nav.slug == nav):
            characteristic = Characteristic.objects.filter(kitchen=product)
            image = Img.objects.filter(product=product)
            context = {
                "product": product,
                "image_list": image,
                "characteristic_list": characteristic,
            }
            if product.nav:
                product_list = Product.objects.filter(nav=product.nav).exclude(slug=product.slug).order_by('name')[:3]
                context["title"] = product.nav
            elif product.show_nav:
                product_list = Product.objects.filter(show_nav=product.show_nav).exclude(slug=product.slug).order_by('name')[:3]
                context["title"] = product.show_nav
            context["product_list"] = product_list
            context["header"] = ""
            context["description"] = ""
            return render(request, "vivakitchen/product/product_detail.html", context)
        else:
            return render(request, "vivakitchen/none.html")




