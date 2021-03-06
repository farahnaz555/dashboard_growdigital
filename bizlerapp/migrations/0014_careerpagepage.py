# Generated by Django 3.2.4 on 2021-07-26 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizlerapp', '0013_portfoliopage'),
    ]

    operations = [
        migrations.CreateModel(
            name='careerpagepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
                ('long_description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='static/images/')),
                ('slug', models.SlugField(null=True)),
            ],
        ),
    ]
