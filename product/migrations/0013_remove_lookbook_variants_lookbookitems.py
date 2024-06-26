# Generated by Django 4.2.4 on 2024-04-22 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0012_remove_collection_tags_remove_products_tags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lookbook',
            name='variants',
        ),
        migrations.CreateModel(
            name='LookBookItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated At')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('deleted_at', models.DateTimeField(auto_now=True, verbose_name='Deleted At')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL, verbose_name='Deleted By')),
                ('look_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='look_book_items', to='product.lookbook', verbose_name='Look Book')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='look_book_product', to='product.products', verbose_name='Product')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
    ]
