# Generated by Django 4.1.7 on 2023-05-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_alter_characteristic_kitchen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='chapter',
            field=models.CharField(choices=[('KITCHEN', 'Кухни'), ('CABINETS', 'Шкафы'), ('BATHROOM', 'Ванные'), ('SOFAS', 'Диваны'), ('GARDEN_FURNITURE', 'Садовая мебель'), ('CHANDELIER', 'Люстры'), ('LAMP', 'Светильники'), ('ALARM_SYSTEMS', 'Трековые системы'), ('CEILING_LIGHT', 'Потолочные'), ('PORTFOLIO', 'Портфолио')], default='KITCHEN', max_length=100, verbose_name='Раздел'),
        ),
    ]
