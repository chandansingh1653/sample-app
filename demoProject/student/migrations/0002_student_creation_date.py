# Generated by Django 4.1.7 on 2023-03-13 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='creation_date'),
            preserve_default=False,
        ),
    ]