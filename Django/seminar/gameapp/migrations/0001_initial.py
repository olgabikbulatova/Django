# Generated by Django 4.2.7 on 2023-11-29 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headtails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=20)),
                ('result_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
