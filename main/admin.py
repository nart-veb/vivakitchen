from django.contrib import admin
from django import forms

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget




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
    list_display = ('name', 'chapter')
    prepopulated_fields = {'slug': ('name',)}  # new
    list_filter = ('chapter',)
    form = ProductAdminForm
    inlines = [ProductImgInline]


admin.site.register(Img)
admin.site.register(Slider)


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('kitchen', 'property', 'value')
    list_filter = ('kitchen',)

# Register your models here.
