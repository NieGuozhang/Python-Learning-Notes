# Generated by Django 3.0.6 on 2020-05-31 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='ddate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
