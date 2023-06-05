# Generated by Django 4.1.7 on 2023-05-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_product_price_alter_product_property_0_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Главная картинка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Картинка для чертежа'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_0',
            field=models.CharField(blank=True, default=123, max_length=200, verbose_name='Свойство 0 (отображающее в разделе)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_1',
            field=models.CharField(blank=True, default=123, max_length=200, verbose_name='Свойство 1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_10',
            field=models.CharField(blank=True, default=21323, max_length=200, verbose_name='Свойство 10'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_2',
            field=models.CharField(blank=True, default=213, max_length=200, verbose_name='Свойство 2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_3',
            field=models.CharField(blank=True, default=2314213, max_length=200, verbose_name='Свойство 3'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_4',
            field=models.CharField(blank=True, default=213, max_length=200, verbose_name='Свойство 4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_5',
            field=models.CharField(blank=True, default=123241, max_length=200, verbose_name='Свойство 5'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_6',
            field=models.CharField(blank=True, default=12432, max_length=200, verbose_name='Свойство 6'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_7',
            field=models.CharField(blank=True, default=12342, max_length=200, verbose_name='Свойство 7'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_8',
            field=models.CharField(blank=True, default=1232, max_length=200, verbose_name='Свойство 8'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='property_9',
            field=models.CharField(blank=True, default=124241, max_length=200, verbose_name='Свойство 9'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_0',
            field=models.CharField(blank=True, default=124324, max_length=200, verbose_name='Значение 0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_1',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_10',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 10'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_2',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_3',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 3'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_4',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_5',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 5'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_6',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 6'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_7',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 7'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_8',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 8'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='value_9',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Значение 9'),
            preserve_default=False,
        ),
    ]
