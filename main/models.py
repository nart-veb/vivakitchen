from django.db import models
from django.urls import reverse

class Brand(models.Model):
    '''Бренды'''
    name = models.CharField("Наименование страницы", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Collection(models.Model):
    '''Коллекции'''
    name = models.CharField("Наименование страницы", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"


class Slider (models.Model):
    "Слайдер"
    name = models.CharField("Заголовок", max_length=150)
    name_b = models.CharField("Продолжение заголовка (жирный)", max_length=150)
    image = models.ImageField("Картинка", upload_to="images/")
    description_a = models.CharField("Текст кнопки", max_length=150)
    path_a = models.CharField("Ссылка", max_length=150)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"


class Img(models.Model):
    product = models.ForeignKey("Product", on_delete = models.CASCADE, related_name="images")
    image = models.ImageField("Картинка", upload_to="images/")


class Nav(models.Model):
    '''Меню'''
    name = models.CharField("Наименование страницы", max_length=200)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"


class ShowNav(models.Model):
    '''Подпункты'''
    name = models.CharField("Наименование страницы", max_length=200, blank=True)
    nav = models.ForeignKey(Nav, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подпункт меню"
        verbose_name_plural = "Подпункты меню"


class ImgPage(models.Model):
    page = models.ForeignKey("Page", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Картинка", upload_to="images/")

class Page(models.Model):
    '''Статичная страница (подпункт)'''
    name = models.CharField("Наименование страницы", max_length=200, blank=True)
    description = models.TextField("Описание", blank=True)
    nav = models.ForeignKey(Nav, on_delete=models.CASCADE, blank=True, null=True)
    show_nav = models.ForeignKey(ShowNav, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статичная страница"
        verbose_name_plural = "Статичные страницы"


class Product(models.Model):
    "Товар"
    name = models.CharField("Название товара", max_length=200)
    nav = models.ForeignKey(Nav, on_delete=models.CASCADE, blank=True, null=True)
    show_nav = models.ForeignKey(ShowNav, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True, null=True)
    _OUTPUT_TO_PORTFOLIO = [
        ('0', 'Нет'),
        ('1', 'Да'),
    ]
    portfolio = models.CharField(max_length=100, choices=_OUTPUT_TO_PORTFOLIO,
                                 verbose_name="Вывести на главную (портфолио)", default='0')

    _OUTPUT_TO_KITCHEN = [
        ('0', 'Нет'),
        ('1', 'Да'),
    ]
    kitchen = models.CharField(max_length=100, choices=_OUTPUT_TO_KITCHEN, verbose_name="Вывести на главную (новинки)",
                               default='0')
    _NOVELTY_TO_KITCHEN = [
        ('0', 'Нет'),
        ('1', 'Да'),
    ]
    novelty = models.CharField(max_length=100, choices=_NOVELTY_TO_KITCHEN, verbose_name="Новинка ?",
                               default='0')
    price = models.CharField("Цена", max_length=200, blank=True)
    description = models.TextField("Описание", blank=True)
    avatar = models.ImageField("Главная картинка", upload_to="images/", blank=True)
    value_left = models.CharField("Значение слева", max_length=200, blank=True)
    value_right = models.CharField("Значение справа", max_length=200, blank=True)
    image = models.ImageField("Картинка для чертежа", upload_to="images/", blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Characteristic (models.Model):
    '''Характеристика'''
    property = models.CharField("Свойство", max_length=200, blank=True)
    value = models.CharField("Значение", max_length=200, blank=True)
    kitchen = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.kitchen.name

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"


class Process(models.Model):
    '''Процесс'''
    name = models.CharField("Заголовок", max_length=200)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Процесс"
        verbose_name_plural = "Процессы"

# Create your models here.
