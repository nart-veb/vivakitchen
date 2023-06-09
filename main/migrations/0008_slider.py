# Generated by Django 4.1.7 on 2023-04-30 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_furniture_kitchen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('path_a', models.CharField(max_length=150, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
            },
        ),
    ]
