# Generated by Django 4.2 on 2023-06-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_blockedipmodel_urlfrommodel"),
    ]

    operations = [
        migrations.RenameField(
            model_name="urlfrommodel",
            old_name="now_url",
            new_name="url_to",
        ),
        migrations.AlterField(
            model_name="urlfrommodel",
            name="url_from",
            field=models.URLField(help_text="url, from which you are going"),
        ),
    ]
