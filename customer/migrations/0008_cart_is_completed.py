# Generated by Django 4.2.4 on 2024-04-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0007_reviewimage_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="is_completed",
            field=models.BooleanField(default=False, verbose_name="Cart Completed"),
        ),
    ]
