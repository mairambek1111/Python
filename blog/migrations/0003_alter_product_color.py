# Generated by Django 5.0.3 on 2024-03-07 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_brand_photo_alter_color_code_remove_product_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, to='blog.color'),
        ),
    ]