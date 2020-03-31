# Generated by Django 3.0.4 on 2020-03-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res', models.CharField(default='User name', max_length=100)),
                ('title', models.CharField(default='Post title', max_length=200)),
                ('desc', models.TextField(default='description')),
                ('img', models.ImageField(default='img/logo.png', upload_to='pics')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]