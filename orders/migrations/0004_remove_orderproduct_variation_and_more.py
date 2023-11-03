# Generated by Django 4.2.6 on 2023-11-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_variation_managers'),
        ('orders', '0003_remove_orderproduct_color_remove_orderproduct_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]