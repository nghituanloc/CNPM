# Generated by Django 4.2.6 on 2023-12-15 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
