# Generated by Django 4.2.3 on 2023-07-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(verbose_name='Password'),
        ),
    ]
