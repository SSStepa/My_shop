# Generated by Django 4.2 on 2023-06-06 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_alter_productmodel_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="category",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="shop.categorymodel"),
        ),
    ]