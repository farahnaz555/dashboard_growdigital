# Generated by Django 3.2.3 on 2021-06-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceandpackagesapp', '0003_priceandpackagesmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceandpackagesmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
