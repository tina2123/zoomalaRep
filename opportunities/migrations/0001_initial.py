# Generated by Django 3.0.4 on 2020-03-31 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default=' ', max_length=100)),
                ('title', models.CharField(default=' ', max_length=200)),
                ('desc', models.TextField(default=' ')),
                ('img', models.ImageField(default='img/logo.png', upload_to='pics')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
