# Generated by Django 4.1.7 on 2023-05-30 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_characteristic_kitchen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characteristic',
            old_name='kitchen',
            new_name='product',
        ),
    ]