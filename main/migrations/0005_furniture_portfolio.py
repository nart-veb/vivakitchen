# Generated by Django 4.1.7 on 2023-04-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_furniture_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='portfolio',
            field=models.CharField(choices=[('0', 'Нет'), ('1', 'Да')], default='1', max_length=100, verbose_name='Вывести на главную (портфолио)'),
        ),
    ]
