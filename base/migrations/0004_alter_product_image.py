# Generated by Django 4.2.6 on 2023-10-30 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]
