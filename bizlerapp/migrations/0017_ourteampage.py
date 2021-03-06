# Generated by Django 3.2.4 on 2021-07-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizlerapp', '0016_customerreviewpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourteampage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('designation', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]
