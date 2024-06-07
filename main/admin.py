from django.contrib import admin
from django import forms

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


admin.site.site_header = "Админка VivaKitchen"

class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductImgInline(admin.TabularInline):
    model = Img
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'nav')
    prepopulated_fields = {'slug': ('name',)}  # new
    list_filter = ('nav',)
    form = ProductAdminForm
    inlines = [ProductImgInline]












class ImgPageInline(admin.TabularInline):
    model = ImgPage
    extra = 1

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ImgPageInline]










admin.site.register(Img)
admin.site.register(Slider)


admin.site.register(Nav)
admin.site.register(ShowNav)

admin.site.register(Brand)
admin.site.register(Collection)

admin.site.register(Process)

@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('kitchen', 'property', 'value')
    list_filter = ('kitchen',)

# Register your models here.
