# Generated by Django 4.2.4 on 2024-03-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("masterdata", "0002_category_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Active"),
        ),
        migrations.AddField(
            model_name="brand",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="brand_tags",
                to="masterdata.tag",
                verbose_name="Tags",
            ),
        ),
    ]
