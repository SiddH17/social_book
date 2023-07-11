# Generated by Django 4.2.3 on 2023-07-10 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0005_profiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(null=True)),
                ('designation', models.CharField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Profiles',
        ),
    ]