# Generated by Django 3.2.14 on 2023-10-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onroadservice', '0008_request_service_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='rating_reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('Ratings', models.CharField(max_length=100)),
                ('Reviews', models.CharField(max_length=100)),
                ('Worker', models.CharField(max_length=100)),
            ],
        ),
    ]
