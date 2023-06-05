# Generated by Django 4.1.7 on 2023-04-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='conclusion',
            field=models.ManyToManyField(related_name='kitchen_conclusion', to='main.conclusion', verbose_name='Вывод на главную'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='style',
            field=models.ManyToManyField(related_name='kitchen_style', to='main.style', verbose_name='Стили'),
        ),
    ]