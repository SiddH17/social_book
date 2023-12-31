# Generated by Django 4.2.3 on 2023-07-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email ID')),
                ('phone', models.PositiveBigIntegerField(unique=True, verbose_name='Phone no.')),
            ],
        ),
    ]
