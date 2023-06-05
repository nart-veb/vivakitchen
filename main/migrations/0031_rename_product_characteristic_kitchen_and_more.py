# Generated by Django 4.1.7 on 2023-05-30 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characteristic',
            old_name='product',
            new_name='kitchen',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='kitchen',
        ),
        migrations.AddField(
            model_name='product',
            name='portfolio_chapter',
            field=models.CharField(choices=[('0', 'Нет'), ('1', 'Да')], default='0', max_length=100, verbose_name='Портфолио'),
        ),
    ]