# Generated by Django 4.1.7 on 2023-05-30 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_alter_characteristic_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characteristic',
            old_name='product',
            new_name='kitchen',
        ),
    ]
