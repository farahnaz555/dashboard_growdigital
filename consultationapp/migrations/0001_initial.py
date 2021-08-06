# Generated by Django 3.1.7 on 2021-04-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='consultationpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField(max_length=11)),
            ],
        ),
    ]