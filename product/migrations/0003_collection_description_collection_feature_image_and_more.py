# Generated by Django 4.2.4 on 2024-03-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("masterdata", "0003_brand_is_active_brand_tags"),
        ("product", "0002_alter_products_categories_alter_products_condition"),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="collection",
            name="feature_image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="collections/image",
                verbose_name="Feature Image",
            ),
        ),
        migrations.AddField(
            model_name="collection",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="collection_tags",
                to="masterdata.tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="collections",
            field=models.ManyToManyField(
                related_name="product_collections",
                to="product.variant",
                verbose_name="Collections",
            ),
        ),
    ]
