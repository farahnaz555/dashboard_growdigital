# Generated by Django 3.1.7 on 2021-04-23 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopage',
            name='image',
            field=models.ImageField(upload_to='portfolioapp/images/'),
        ),
    ]
