# Generated by Django 3.2.4 on 2021-07-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizlerapp', '0015_businesspartnerpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerreviewpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
    ]
