# Generated by Django 4.1.7 on 2023-03-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=100)),
                ('last_Name', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=10)),
            ],
        ),
    ]
