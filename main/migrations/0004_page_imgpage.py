# Generated by Django 4.2.1 on 2024-05-31 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_nav_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Наименование страницы')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('shownav', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.shownav')),
            ],
            options={
                'verbose_name': 'Раздел интерьера',
                'verbose_name_plural': 'Разделы интерьера',
            },
        ),
        migrations.CreateModel(
            name='ImgPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.page')),
            ],
        ),
    ]
