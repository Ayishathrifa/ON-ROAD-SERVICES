# Generated by Django 3.2.14 on 2023-10-31 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onroadservice', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='own_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WORKER', models.CharField(max_length=200)),
                ('SERVICE', models.CharField(max_length=200)),
                ('Amount', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('OWN_SERVICE', models.CharField(max_length=200)),
                ('USER', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
