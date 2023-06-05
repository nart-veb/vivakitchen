from django.shortcuts import render
from .functions import *
from django.views.generic.base import View
from .models import *

class IndexView(View):
    # главная страница
    def get(self, request):
        slide = Slider.objects.all()
        product_portfolio = Product.objects.filter(portfolio=1, chapter="KITCHEN")
        product_vip = Product.objects.filter(kitchen="1", chapter="KITCHEN")
        context = {
            "slide_list": slide,
            "product_portfolio_list": product_portfolio,
            "product_vip_list": product_vip,
        }
        return render(request, 'vivakitchen/index.html', context)

class Kitchen(View):
    # кухни
    def get_index(request):
        context = product_index("KITCHEN", "product_list")
        context["title"] = "кухни"
        context["header"] = "каталог кухонь"
        context["description"] = "Уютная красивая кухня с современной мебелью может стать любимым местом отдыха для любой семьи, ведь так приятно провести время с близкими в расслабляющей обстановке. Если же гарнитур не только эстетичен, но и удобен в эксплуатации, практичен, то хозяйки с большим удовольствием проводят время на кухне, радуя семью новыми кулинарными шедеврами."
        return render(request, "vivakitchen/product/product_index.html", context)

    def get_detail(request, slug):
        context = product_detail(slug, "product")
        context["title"] = "кухни"
        context["header"] = "кухня"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_detail.html", context)

    # def get_absolute_url(self):
    #     return reverse('product-detail', kwargs={'slug': self.slug}) # new



class Wardrobes(View):
    # шкафы лист
    def get_index(request):
        context = product_index("CABINETS", "product_list")
        context["title"] = "шкафы"
        context["header"] = "каталог шкафов"
        context["description"] = "Уютная красивая кухня с современной мебелью может стать любимым местом отдыха для любой семьи, ведь так приятно провести время с близкими в расслабляющей обстановке. Если же гарнитур не только эстетичен, но и удобен в эксплуатации,практичен, то хозяйки с большим удовольствием проводят время на кухне, радуя семью новыми кулинарными шедеврами."
        return render(request, "vivakitchen/product/product_index.html", context)

    def get_detail(request, slug):
        context = product_detail(slug, "product")
        context["title"] = "шкафы"
        context["header"] = "шкаф"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_detail.html", context)

    # def get_absolute_url(self):
    #     return reverse('wardrobes-detail', kwargs={'slug': self.slug}) # new



class Bathroom(View):
    # ванны лист
    def get_index(request):
        context = product_index("BATHROOM", "product_list")
        context["title"] = "ванные"
        context["header"] = "ванные на заказ"
        context["description"] = "Каталог мебели для ванных Viva Kitchen — это набор идеальных решений по максимально эффективному использованию пространства ванных комнат. Разнообразие различных тумб, пеналов, подвесных шкафов, зеркал, настенных полок и аксессуаров позволяет создавать уникальные композиции, всегда практичные и эстетически привлекательные."
        return render(request, "vivakitchen/product/product_index.html", context)

    def get_detail(request, slug):
        context = product_detail(slug, "product")
        context["title"] = "ванные"
        context["header"] = "ванна"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_detail.html", context)

    # def get_absolute_url(self):
    #     return reverse('bathroom-detail', kwargs={'slug': self.slug})


class Sofas(View):
    # диваны лист
    def get_index(request):
        context = product_index("SOFAS", "product_list")
        context["title"] = "диваны"
        context["header"] = "каталог диванов"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_index.html", context)

    def get_detail(request, slug):
        context = product_detail(slug, "product")
        context["title"] = "диваны"
        context["header"] = "диван"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_detail.html", context)

    # def get_absolute_url(self):
    #     return reverse('sofas-detail', kwargs={'slug': self.slug})  # new

class Garden(View):
    # мебель лист
    def get_index(request):
        context = product_index("GARDEN_FURNITURE", "product_list")
        context["title"] = "мебель"
        context["header"] = "Мебель ждя вашего дома"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_index.html", context)

    def get_detail(request, slug):
        context = product_detail(slug, "product")
        context["title"] = "мебель"
        context["header"] = ""
        context["description"] = ""
        return render(request, "vivakitchen/product/product_detail.html", context)

    # def get_absolute_url(self):
    #     return reverse('sofas-detail', kwargs={'slug': self.slug})



class Light():
    # свет лист
    def get_chandelier(request):
        context = product_index("CHANDELIER", "product_list")
        context["title"] = "люстры"
        context["header"] = "Каталог люстр"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_index.html", context)

    def get_lamp(request):
        context = product_index("LAMP", "product_list")
        context["title"] = "светильники"
        context["header"] = "Каталог светильников"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_index.html", context)

    def get_system(request):
        context = product_index("ALARM_SYSTEMS", "product_list")
        context["title"] = "трековые системы"
        context["header"] = "Каталог трековых систем"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_index.html", context)

    def get_ceiling(request):
        context = product_index("CEILING_LIGHT", "product_list")
        context["title"] = "потолочный свет"
        context["header"] = "Каталог потолочного света"
        context["description"] = ""
        return render(request, "vivakitchen/product/product_index.html", context)

    def get_detail(request, slug):
        context = product_detail(slug, "product")
        context["title"] = "свет"
        context["header"] = ""
        context["description"] = ""
        return render(request, "vivakitchen/product/product_detail.html", context)




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
        return render(request, 'vivakitchen/buyer.html')

class Contact(View):
    def get(self, request):
        return render(request, 'vivakitchen/contact.html')

class About(View):
    def get(self, request):
        return render(request, 'vivakitchen/about.html')


