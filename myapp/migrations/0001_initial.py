# Generated by Django 4.2.3 on 2023-07-19 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string1', models.CharField(max_length=255)),
                ('string2', models.CharField(max_length=255)),
                ('string3', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
