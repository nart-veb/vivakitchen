# Generated by Django 4.1.7 on 2023-05-26 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_product_novelty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(blank=True, max_length=200, verbose_name='Свойство')),
                ('value', models.CharField(blank=True, max_length=200, verbose_name='Значение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
    ]
